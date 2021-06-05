############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

###############Libraries and Prerequisites###############
import requests
import re
import string
import collections

###############Helper Functions###############
def dl_book(url, filename):
    ''' Downloads the content of a html page.
        
    @param url: the url of the html page to download the content from
    @param filename: the name of the destination file for the download
    @return: None
    '''
    r = requests.get(url)
    open(filename, 'wb').write(r.content)

def split_file(filename):
    ''' Reads input file, strips HTML and digits and makes text lowercase, and separates words at each \s.
    
    @param filename: name of the file to read 
    @return: a list of strings where each elem is a word in the input file
    '''
    with open(filename) as f:
        content = f.read().lower()
        content = re.sub('<.+?>|[0-9]', '', content) # Strip HTML and any digits with regex
        content = content.replace('rdquo', '').replace('mdash', ' ')\
             .replace('rsquos', '').replace('ldquo', '')\
                 .replace('rsquo', '')  # removing extraneous html formatting
        content = content.translate(content.maketrans('', '', string.punctuation)).split() # remove punctuation

    return content

def rm_front_end(filename):
    ''' Removes the unnecessary beginning and ending parts of Proj Gutenberg Books.

    @param filename: name of the txt file to format
    @return: None
    '''
    with open(filename) as f:
        content = f.read().lower()
        start_index = content.find('*** start')
        end_index = content.find('*** end')
        content = content[start_index:end_index]

        # Edge Cases
        if 'end of the project gutenberg ebook' in content:
            edge_index = content.find('end of the project gutenberg ebook')
            content = content[:edge_index]

    open(filename, 'w').write(content)

def book_stats(words):
    ''' Calculates various stats on the given contents of a list of words.

    @param words: list of strings with words
    @return: a Counter object from collections library
    '''
    counter = collections.Counter(words)
        
    return counter

def word_check():
    ''' Prompts the user to input as many words as they want to check if they exist in
    a list of words.

    @param words_list: the list of words that we are comparing the user input to
    @return: a list of words stating whether user input exists or not 
    '''

###############Main Script###############
dl_book('https://www.gutenberg.org/files/2600/2600-h/2600-h.htm', 'w&p.txt')
dl_book('https://www.gutenberg.org/files/98/98-h/98-h.htm', 'two_cities.txt')
dl_book('https://www.gutenberg.org/files/174/174-h/174-h.htm', 'gray.txt')
rm_front_end('w&p.txt')
rm_front_end('two_cities.txt')
rm_front_end('gray.txt')
text_wp = split_file('w&p.txt')
text_cities = split_file('two_cities.txt')
text_gray = split_file('gray.txt')
counter_wp = book_stats(text_wp)
counter_cities = book_stats(text_cities)
counter_gray = book_stats(text_gray)

most_common_wp = zip([x[0] for x in counter_wp.most_common(20)], [x[1] for x in \
    counter_wp.most_common(20)])
least_common_wp = zip([x[0] for x in counter_wp.most_common()[:-20-1:-1]], [x[1] for x in \
    counter_wp.most_common()[:-20-1:-1]])
most_common_cities = zip([x[0] for x in counter_cities.most_common(20)], [x[1] for x in \
    counter_cities.most_common(20)])
least_common_cities = zip([x[0] for x in counter_cities.most_common()[:-20-1:-1]], [x[1] for x in \
    counter_cities.most_common()[:-20-1:-1]])
most_common_gray = zip([x[0] for x in counter_gray.most_common(20)], [x[1] for x in \
    counter_gray.most_common(20)])
least_common_gray = zip([x[0] for x in counter_gray.most_common()[:-20-1:-1]], [x[1] for x in \
    counter_gray.most_common()[:-20-1:-1]])

print('The 20 Most Frequent Words in War & Peace')
for k, v in most_common_wp:
    print(k + ': ' + str(v))
print()

print('The 20 Least Frequent Words in War & Peace')
for k, v in least_common_wp:
    print(k + ': ' + str(v))
print()

print('The 20 Most Frequent Words in A Tale of Two Cities')
for k, v in most_common_cities:
    print(k + ': ' + str(v))
print()

print('The 20 Least Frequent Words in A Tale of Two Cities')
for k, v in least_common_cities:
    print(k + ': ' + str(v))
print()

print('The 20 Most Frequent Words in The Picture of Dorian Gray')
for k, v in most_common_gray:
    print(k + ': ' + str(v))
print()

print('The 20 Least Frequent Words in The Picture of Dorian Gray')
for k, v in least_common_gray:
    print(k + ': ' + str(v))