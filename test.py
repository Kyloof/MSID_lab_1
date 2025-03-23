import pandas as pd

# Your dictionary
stats_dict = {
    'sofifa_id': {
        'count': 19239.0,
        'mean': 231468.08695878164,
        'std': 27039.717497127018,
        'min': 41.0,
        '5%': 184133.9,
        '50%': 236543.0,
        '95%': 263046.1,
        'max': 264640.0
    }
}

# Convert the dictionary to a DataFrame
stats_df = pd.DataFrame(stats_dict)

# Transpose the DataFrame to have statistical metrics as rows
stats_df = stats_df.T

# Add the feature name as the first column
stats_df.insert(0, 'Feature', stats_df.index)

# Save the DataFrame to CSV, index=False to avoid index being saved as a separate column
stats_df.to_csv('output_numeric.csv', index=False)

print("Statystyki zostały zapisane do pliku 'statistics.csv'")
