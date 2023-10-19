from config import FILE_PATH
import pandas as pd

def delete_housing(housing_id):
    df = pd.read_csv(FILE_PATH)
    df = df.drop(df[df['id'] == housing_id].index)
    df.to_csv(FILE_PATH, index=False)