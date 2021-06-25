import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.subplots(figsize=(15,5))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    sealevel_regression_1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x_range = list(df['Year'])
    for i in range(2014, 2051):
        x_range.append(i)
    m = sealevel_regression_1.slope
    b = sealevel_regression_1.intercept
    plt.xlim(left=1880, right=2050)
    plt.xticks([float(x) for x in range(1850, 2076, 25)])
    plt.plot(x_range, [x * m + b for x in x_range], c='red', label='1880-2050')

    # Create second line of best fit
    x_range_2 = [i for i in range(2000, 2051)]
    y_values = df['CSIRO Adjusted Sea Level'].loc[df['Year'] >= 2000]
    sealevel_regression_2 = linregress(x=df['Year'].loc[df['Year'] >= 2000], y=y_values)
    m2 = sealevel_regression_2.slope
    b2 = sealevel_regression_2.intercept
    plt.plot(x_range_2, [x * m2 + b2 for x in x_range_2], c='green', label='2000-2050')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()