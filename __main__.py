from load_data import load_data

from plot_creator import create_plot_errorbars, display_plots, create_displot, create_heatmap, create_boxplot, create_regplot, create_violinplot
from project_statistics import get_numeric_stats, generate_statistic_from_file_path
result = generate_statistic_from_file_path("UltimateClassicRock.csv", "UltimateClassicRock.csv")
print(result)  # Check what is being returned

df = load_data("UltimateClassicRock.csv")


#create_plot_errorbars(get_numeric_stats())

create_boxplot(df, "Year", "Tempo", "Tempo by each year")
create_boxplot(df, "Mode", "Tempo", "Tempo by mode")
create_boxplot(df, "Time_Signature", "Tempo","")

create_violinplot(df, "Mode", "Popularity", "123")
create_violinplot(df, "Time_Signature", "Popularity", "123")


create_displot(df, "Year", "Years")
create_displot(df, "Time_Signature", "Years")

numeric_columns = [
        "Duration", "Danceability", "Energy", "Key", "Loudness", 
        "Speechiness", "Acousticness", "Instrumentalness", "Liveness", 
        "Valence", "Popularity", "Tempo"
    ]
create_regplot(df, "Loudness", "Energy")
create_regplot(df, "Duration", "Popularity")
create_heatmap(df, numeric_columns)


display_plots()




'''
create_displot(df, "Year", "YTe", "Key")
create_heatmap(df, ["Tempo", "Popularity", "Valence"])
create_violinplot(df, "Mode", "Popularity", "!@3")
create_regplot(df, "Duration", "Popularity")
'''