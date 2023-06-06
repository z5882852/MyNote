import pandas as pd

def read_csv(file_path, sep):
    file = pd.read_csv(file_path, sep=sep, header=0, engine='python', encoding='utf-8', keep_default_na=False)
    return file



