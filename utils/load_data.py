import pandas as pd
from utils import convert_duration_to_minutes
def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            
            df = pd.read_csv(file_path, low_memory=False)
            df['Duration'] = df['Duration'].apply(convert_duration_to_minutes)
            return df
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Nieobsługiwany format pliku!")
    except Exception as e:
        print(f"Błąd podczas wczytywania danych: {e}")
        return None
    
