import seaborn as sns
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def create_boxplot(database, x_axis, y_axis, title):
    plot = sns.catplot(data=database, x=x_axis, y=y_axis, kind="box", height=7, aspect=2)
    ax = plot.ax
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.tick_params(axis="x", rotation=45)  
    plt.show()


def create_violinplot(database, x_axis, y_axis, title):
    plot = sns.catplot(data=database, x=x_axis, y=y_axis, kind="violin", height=7, aspect=2)
    ax = plot.ax
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    plt.show()
    
def create_displot(database, x, title, hue=None):
    if hue is None:
        plot = sns.displot(database, x=x, multiple="dodge",  height=7, aspect=2)
    else:
        plot = sns.displot(database, x=x, hue=hue, height=7, aspect=2)
    ax = plot.ax
    ax.set_title(title)
    ax.set_xlabel(x)
    plt.show()

def create_plot_errorbars(df):
    attributes = df.index
    means = df["mean"]
    std_devs = df["std"]

    num_plots = len(attributes)
    num_columns = 3 
    num_rows = (num_plots // num_columns) + (num_plots % num_columns > 0)
    
    _, axes = plt.subplots(
        nrows=num_rows, ncols=num_columns, figsize=(15, num_rows * 4), sharex=False
    )

    axes = axes.flatten()

    numeric_columns = [
        "Duration", "Danceability", "Energy", "Key", "Loudness", 
        "Speechiness", "Acousticness", "Instrumentalness", "Liveness", 
        "Valence", "Tempo", "Popularity", 
    ]
    
    for i, attr in enumerate(attributes):
        axes[i].errorbar(
            x=attr,
            y=means[attr],
            yerr=std_devs[attr],
            fmt="o",
            capsize=5,
            color="blue",
        )
        axes[i].set_ylabel("Mean Value")
        axes[i].set_title(f"{numeric_columns[attr]} (mean ± std)")
        axes[i].grid(True)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5, wspace=0.3)
    plt.show()

def create_heatmap(df, columns):
    correlation_matrix = df[columns].corr()
    
    plt.figure(figsize=(10, 7)) 
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, square=True)
    
    ax.set_title("Heatmap of Values")
    plt.show()




def create_regplot(data, x, y, title):
    plt.figure(figsize=(14, 7)) 
    ax = sns.regplot(x=x, y=y, data=data)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.show()

