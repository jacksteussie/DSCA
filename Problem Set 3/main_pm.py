############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

############### Libraries and Prerequisites ###############
from bs4 import BeautifulSoup
import time 
import requests
import sys
import csv
import nltk
import pandas as pd
import numpy as np
import re
import sqlite3
from os import path
import subprocess

############### Helper Functions ###############
def scrape(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	html = list(soup.children)[11] # Separate the html tags and the content they contain from the rest of the page
	body = list(html.children)[5]  # Get the body of the html text

	# Now we get various info related to the book that are available on the webpage itself
	book_data = dict()
	book_entry = {header.get_text(strip=True): header.find_next_sibling('td').get_text(strip=True) \
		for header in soup.select('table.table-striped tr th')}
	book_entry['price'] = book_entry.pop('Price (excl. tax)')			# Make price w/o tax our measure of true price since sales tax varies by 
	book_entry['price_yes_tax'] = book_entry.pop('Price (incl. tax)')	# location (although in this case the taxes are all 0% so it does not really matter)
	book_entry['availability'] = book_entry.pop('Availability')
	book_entry['product_type'] = book_entry.pop('Product Type')
	book_entry['upc'] = book_entry.pop('UPC')
	book_entry['tax'] = book_entry.pop('Tax')
	book_entry['num_reviews'] = book_entry.pop('Number of reviews')
	book_entry['title'] = body.find('h1').get_text()
	book_entry['rating'] = body.find('p', class_='star-rating').get_attribute_list('class')[1]
	book_entry['genre'] = body.find_all('a')[3].get_text()
	book_entry['description'] = body.find_all('p')[3].get_text()

	return book_entry

############### Main Script ###############
book_data = list()
for arg in sys.argv:
	if arg == sys.argv[0]:
		continue

	book_entry = scrape(arg)
	book_data.append(book_entry)
	time.sleep(2)


help_dict = {			# Clean-up tiiiiime (╯°□°)╯︵ ┻━┻ ---> ┬─┬ノ( º _ ºノ)
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
word_vectors = list()
for entry in book_data:
	entry['description'] = ''.join(filter(whitelist.__contains__, entry['description']))
	entry['description'] = entry['description'].replace('\xa0', '')
	entry['description'] = nltk.word_tokenize(entry['description'])
	entry['rating'] = ''.join(help_dict[ele] for ele in entry['rating'].lower().split())
	entry['availability'] = re.sub('[^0-9]', '', entry['availability'])
	entry['price'] = round(float(re.sub('£', '', entry['price'])) * 1.411, 2) # GBP to USD conversion

	# get word freuqncy
	fdist = nltk.FreqDist(entry['description'])

    # Convert to Pandas dataframe
	df_fdist = pd.DataFrame.from_dict(fdist, orient='index')
	df_fdist.columns = ['Frequency']

    # Sort by word frequency
	df_fdist.sort_values(by=['Frequency'], ascending=False, inplace=True)

    # Add word index
	number_of_words = df_fdist.shape[0]
	df_fdist['word_index'] = list(np.arange(number_of_words)+1)

    # replace rare words with index zero
	cutoff = 1
	frequency = df_fdist['Frequency'].values
	word_index = df_fdist['word_index'].values
	mask = frequency <= cutoff
	word_index[mask] = 0
	df_fdist['word_index'] = word_index
    
    # Convert pandas to dictionary
	word_dict = df_fdist['word_index'].to_dict()

	text_numbers = list()
	for string in entry['description']:
		string_numbers = [word_dict[word] for word in entry['description']]
		text_numbers.append(string_numbers)
	
	entry['description'] = text_numbers

# Export finalized data to csv
keys = book_data[0].keys()
with open('book_data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(book_data)

### SQLite Database Export ###
subprocess.call(['sqlite3', 
				'bookstoscrape.db', '.mode csv', 
				'.import book_data.csv scraped_stuff'])
				
conn = sqlite3.connect('bookstoscrape.db')
cur = conn.cursor()
cur.executescript('''
			DROP TABLE IF EXISTS scraped_books ;
			CREATE TABLE scraped_books (upc, product_type, price, availability, num_reviews, title, rating, genre, description) ;
			INSERT INTO scraped_books SELECT upc, product_type, price, availability, num_reviews, title, rating, genre, description FROM scraped_stuff ;
			SELECT * FROM scraped_books ;
			DROP TABLE IF EXISTS scraped_stuff ; 
			''')
conn.commit()
conn.close()