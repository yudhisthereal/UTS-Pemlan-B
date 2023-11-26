import csv
from config import *
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)


def id_exists(target_id) -> bool:
    with open(get_temp_path(), 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(target_id):
                return True
    return False


def search(data, query, target_column):

    # change missing values (NaN) in target_column to empty string
    data[target_column].fillna('(Empty)', inplace=True)

    filtered_columns = pd.DataFrame()
    if target_column == 'id':
        filtered_data = data[data[target_column] == int(query)]
    elif target_column in ('minimum_nights', 'price'):
        query = int(query)
        filtered_data = data[(data[target_column] <= query)
                             & (data[target_column] >= query - 5)]
    else:
        filtered_data = data[data[target_column].str.contains(
            str(query), case=False)]

    results = filtered_data[COLUMNS_IN_SEARCH]

    if target_column == 'price': 
        results = results.sort_values(
            by=['price', 'availability_365'], ascending=[True, False])


    return results
