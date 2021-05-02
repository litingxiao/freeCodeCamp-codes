import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(1880, 2051)
    plt.plot(x, res.slope * x + res.intercept)

    # Create second line of best fit
    res = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    x = np.arange(2000, 2051)
    plt.plot(x, res.slope * x + res.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()