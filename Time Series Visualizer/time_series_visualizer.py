import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col=0,parse_dates=True,dayfirst=False)

# Clean data
df = df.loc[~((df.value<df.value.quantile(0.025))|
              (df.value>df.value.quantile(0.975)))]

def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(15,6))
    sns.lineplot(data=df,legend=False)
    ax.set(xlabel='Date',ylabel='Page Views',title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month_name()

    df_bar = pd.DataFrame(df_bar.groupby(["year", "month"], sort=False)["value"].mean().round().astype(int))
    df_bar = df_bar.rename(columns={"value": "average_page_views"})
    df_bar = df_bar.reset_index()

    missing_data = {
        "year": [2016, 2016, 2016, 2016],
        "month": ['January', 'February', 'March', 'April'],
        "average_page_views": [0, 0, 0, 0]
    }

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")

    sns.barplot(data=df_bar, x="year", y="average_page_views", hue="month", palette="tab10")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, horizontalalignment='center')
    ax.set(ylabel='Average Page Views',xlabel='Years')



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    
    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(1, 2, figsize=(25, 10))
    
    # Yearly boxplot
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0],hue='year',legend=False)
    ax[0].set(title='Year-wise Box Plot (Trend)',xlabel='Year',ylabel='Page Views')
    
    # Monthly boxplot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=ax[1], hue='month',legend=False)
    ax[1].set(title='Month-wise Box Plot (Seasonality)',xlabel='Year',ylabel='Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
