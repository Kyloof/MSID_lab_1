import pandas as pd
def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path, low_memory=False)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Nieobsługiwany format pliku!")
    except Exception as e:
        print(f"Błąd podczas wczytywania danych: {e}")
        return None
    

print(load_data("players_22.csv"))