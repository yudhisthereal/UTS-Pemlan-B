import csv
from config import *
import pandas as pd

def id_exists(target_id) -> bool:
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(target_id):
                return True
    return False


def search(query, target_column='name'):
    data = pd.read_csv(FILE_PATH)

    # change missing values (NaN) in target_column to empty string
    data[target_column].fillna('(Empty)', inplace=True)

    filtered_columns = pd.DataFrame()
    if target_column == 'id':
        filtered_data = data[data[target_column] == int(query)]
    elif target_column in ('minimum_nights', 'price'):
        query = int(query)
        filtered_data = data[(data[target_column] <= query) & (data[target_column] >= query - 15)]
    else:
        filtered_data = data[data[target_column].str.contains(str(query), case=False)]
        

    selected_columns = ['id', 'name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'availability_365']
    results = filtered_data[selected_columns]
    
    results = results.sort_values(by=['price', 'availability_365', 'number_of_reviews'], ascending=[True, False, False])

    return results

