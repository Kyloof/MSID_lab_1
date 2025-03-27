import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Queue to store plot references
plot_queue = []

import seaborn as sns
import matplotlib.pyplot as plt

def create_boxplot(database, x_axis, y_axis, title):
    plot = sns.catplot(data=database, x=x_axis, y=y_axis, kind="box", height=7, aspect=2)

    ax = plot.ax

    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontweight='light', fontsize='x-large')
    plot_queue.append(plot.figure)

    return plot.figure 

def create_violinplot(database, x_axis, y_axis, title):
    plot = sns.catplot(data=database, x=x_axis, y=y_axis, kind="violin", height=9, aspect=2)
    ax = plot.ax
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontweight='light', fontsize='x-large')
    plot_queue.append(plot.figure)

    return plot.figure 
def create_displot(database, x, title, hue=None):
    if hue is None:
        plot = sns.displot(database, x=x)
    else:
        plot = sns.displot(database, x=x, hue=hue)
    plot.set_titles(title)
    plot.set_axis_labels(x)
    plot_queue.append(plot)

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
    plot_queue.append(plt)

def create_heatmap(df, columns):
    correlation_matrix = df[columns].corr()
    plt.figure(figsize=(12, 8)) 
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, square=True)
    plt.title('Correlation Heatmap')
    plot_queue.append(plt)

def create_regplot(data, x, y):
    plot = sns.regplot(x=x, y=y, data=data)
    plot_queue.append(plot)

def display_plots():
    for plot in plot_queue:
        plot.show()

    plot_queue.clear()
