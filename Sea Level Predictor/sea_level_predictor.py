import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,4))
    ax.scatter(x=df.Year,y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    reg1 = linregress(x=df.Year,y=df['CSIRO Adjusted Sea Level'])

    x1 = np.arange(df.Year.min(),2051,1,dtype=int)
    y1 = reg1.intercept + reg1.slope*x1

    ax.plot(x1,y1,'r', label='reg1')

    # Create second line of best fit
    new_df = df.loc[df.Year>=2000]
    reg2 = linregress(x=new_df.Year,y=new_df['CSIRO Adjusted Sea Level'])

    x2 =np.arange(2000,2051,1,dtype=int)
    y2 = reg2.intercept + reg2.slope*x2

    ax.plot(x2,y2,'r', label='fitted line')

    # Add labels and title
    ax.set(xlabel='Year',ylabel='Sea Level (inches)',title='Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()