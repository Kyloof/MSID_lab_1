from load_data import load_data
from plot_creator import create_plot_errorbars, display_plots, create_displot
from project_statistics import get_numeric_values, get_numeric_stats

df = load_data("UltimateClassicRock.csv")

create_plot_errorbars(get_numeric_stats())
create_displot(df, "Year", "YTe", "Key")
display_plots()