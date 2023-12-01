from config import get_temp_path

def delete_housing(df, housing_id):
    housing_id = int(housing_id)
    df = df.drop(df[df['id'] == housing_id].index)
    df.to_csv(get_temp_path(), index=False)
