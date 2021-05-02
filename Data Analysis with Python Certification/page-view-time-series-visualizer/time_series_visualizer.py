import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
mask = df['value'] <= df['value'].quantile(0.975)
mask &= (df['value'] >= df['value'].quantile(0.025))
df = df.loc[mask]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(df.index, df['value'])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()

    df_bar = df_bar.groupby(['Years', 'Months']).agg({'value': 'mean'}).unstack()

    df_bar.columns = df_bar.columns.get_level_values(1)
    new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar.reindex(columns=new_order)

    # Draw bar plot
    fig = df_bar.plot(figsize=(10,8.2), kind='bar', xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.rename(columns={'value': 'Page Views'})

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))

    sns.boxplot(x=df_box['Year'], y=df_box['Page Views'], orient='v', ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")

    new_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x=df_box['Month'], y=df_box['Page Views'], orient='v', ax=axes[1], order=new_order)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()