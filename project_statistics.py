import pandas as pd
from load_data import load_data
from utils import convert_duration_to_minutes

def generate_statistic_from_file_path(file_path, output_path):
    df = load_data(file_path)

    categorical_columns = [
        "Track", "Artist", "Album", "Year", "Mode", "Time_Signature"
    ]
    
    numeric_columns = [
        "Duration", "Danceability", "Energy", "Key", "Loudness", 
        "Speechiness", "Acousticness", "Instrumentalness", "Liveness", 
        "Valence", "Popularity", "Tempo"
    ]
    

    numeric_stats = {}
    categorical_stats = []
    
    for attr in df.columns:
        missing_values = df[attr].isnull().sum()

        if attr in numeric_columns:
            stats = df[attr].describe(percentiles=[0.05, 0.95])
            numeric_stats[attr] = stats.to_dict()
            numeric_stats[attr]["missing_values"] = missing_values
            
        else:
            value_counts = df[attr].value_counts(normalize=True) * 100
            stats = {
                'attribute': attr,
                'unique_classes_amount': df[attr].nunique(),
                'missing_values': missing_values,
                'class_proportions': value_counts.to_dict()
            }
            categorical_stats.append(stats)
    
    numeric_df = pd.DataFrame(numeric_stats).transpose()
    numeric_df.insert(0, 'attribute', numeric_df.index)
    categorical_df = pd.DataFrame(categorical_stats)
    
    numeric_df.to_csv(output_path.replace('.csv', '_numeric.csv'), index=False)
    categorical_df.to_csv(output_path.replace('.csv','_categorical.csv'), index=False)

    return numeric_df, categorical_df



def get_numeric_values(df):
    numeric_columns = [
        "Duration", "Danceability", "Energy", "Key", "Loudness", 
        "Speechiness", "Acousticness", "Instrumentalness", "Liveness", 
        "Valence", "Tempo", "Popularity"
    ]
    return df[numeric_columns]


def get_categorical_values(df):
    categorical_columns = [
        "Track", "Artist", "Album", "Year", "Mode", "Time_Signature"
    ]
    return df[categorical_columns]


def get_numeric_stats():
    return load_data("UltimateClassicRock_numeric.csv")


def get_categorical_values(df):
    categorical_columns = [
        "Track", "Artist", "Album", "Year", "Mode", "Time_Signature"
    ]
    return df[categorical_columns]