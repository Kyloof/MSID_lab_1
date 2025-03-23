import pandas as pd
from load_data import load_data

def generate_statistic_from_file_path(file_path, output_path):
    df = load_data(file_path)

    numeric_stats = {}
    categorical_stats = []
    
    for attr in df.columns:
        missing_values = df[attr].isnull().sum()

        if df[attr].dtype == 'int64' or df[attr].dtype == 'float64':
            stats = df[attr].describe(percentiles=[0.05, 0.95]).loc[['count','mean','std','min','max','5%','95%']]
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

generate_statistic_from_file_path("players_22.csv", "players_output.csv")