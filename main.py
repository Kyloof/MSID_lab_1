from load_data import load_data
from plot_creator import create_plot_errorbars, create_displot, create_heatmap, create_boxplot, create_regplot, create_violinplot
from project_statistics import get_numeric_stats, generate_statistic_from_file_path

numerical_df, categorical_df = generate_statistic_from_file_path("UltimateClassicRock.csv", "UltimateClassicRock.csv")
numerical_df

categorical_df



create_plot_errorbars(get_numeric_stats())

df = load_data("UltimateClassicRock.csv")

create_boxplot(df, "Year", "Tempo", "Tempo by each year")
create_boxplot(df, "Mode", "Tempo", "Tempo by minor(0) and major(1) mode")
create_boxplot(df, "Time_Signature", "Tempo","Tempo by Time Signature")

create_violinplot(df, "Mode", "Popularity", "Popularity by Mode")
create_violinplot(df, "Time_Signature", "Popularity", "Popularity by Time Signature")

create_displot(df, "Year", "Years displot")
create_displot(df, "Key", "Years", hue="Mode")

numeric_columns = ["Duration", "Danceability", "Energy", "Key", "Loudness", "Speechiness", "Acousticness", "Instrumentalness", "Liveness", "Valence", "Popularity", "Tempo"]
create_heatmap(df, numeric_columns)

create_regplot(df, "Loudness", "Energy", "Linear Regression Loudness vs Energy")


create_regplot(df, "Acousticness", "Energy", "Linear Regression Acousticness vs Energy")


