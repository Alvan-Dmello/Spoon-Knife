import pandas as pd

def load_source_data(path):
    print(f"Loading data from {path}")
    return pd.DataFrame({'col1': [1,2]})