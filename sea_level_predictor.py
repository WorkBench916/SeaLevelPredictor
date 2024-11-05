import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    plt.xlim(1850, 2075)



    # Create first line of best fit
    years1 = list(range(1880, 2051))

    bestFitLine1 = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    slope1, intercept1, *rest1 = bestFitLine1

    seaLevels1 = [(slope1 * year) + intercept1 for year in years1]

    plt.plot(years1, seaLevels1, ls = ':', lw = 3, color = 'green', label = 'first line of best fit')

    # Create second line of best fit
    years2 = list(range(2000, 2051))

    bestFitLine2 = linregress(x = df.loc[df['Year'] >= 2000, 'Year'], y = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])

    slope2, intercept2, *rest2 = bestFitLine2

    seaLevels2 = [slope2 * year + intercept2 for year in years2]

    plt.plot(years2, seaLevels2, ls = '--', lw = 3, color = 'pink', label = 'second line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()