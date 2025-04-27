import pandas as pd

def load_dataset(path='../finall.csv'):
    """
    Load and preprocess the dataset.
    """
    df = pd.read_csv(path)
    df = df.dropna(subset=['next_difficulty'])  # Drop rows with missing target values
    return df
