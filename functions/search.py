import csv
from config import *
import pandas as pd


def id_exists(target_id) -> bool:
    with open(get_temp_path(), 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(target_id):
                return True
    return False


def search(data, query, target_column='name', minimal=False):

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

    selected_columns = COLUMNS_IN_SEARCH if not minimal else COLUMNS_IN_SEARCH_MINIMAL
    results = filtered_data[selected_columns]

    if target_column == 'price': 
        results = results.sort_values(
            by=['price', 'availability_365'], ascending=[True, False])


    return results
