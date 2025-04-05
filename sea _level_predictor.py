import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    future_years = range(df['Year'].min(), 2051)
    line_of_best_fit = [slope * year + intercept for year in future_years]
    plt.plot(future_years, line_of_best_fit, 'r', label='1880-2050 trend')
    
    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    future_years2 = range(2000, 2051)
    line_of_best_fit2 = [slope2 * year + intercept2 for year in future_years2]
    plt.plot(future_years2, line_of_best_fit2, 'g', label='2000-2050 trend')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
