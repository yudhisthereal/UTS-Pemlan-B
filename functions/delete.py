from config import FILE_PATH

def delete_housing(df, housing_id):
    df = df.drop(df[df['id'] == housing_id].index)
    df.to_csv(FILE_PATH, index=False)

