import pandas as pd
from config import COLUMNS_IN_SHOW

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)


def show_filtered(data, sorted_column, ascending):
    results = data[COLUMNS_IN_SHOW]
    results.sort_values(by=sorted_column, ascending=ascending)
    results = results.head(50)

    print('Here\'s your informations:')
    print(results)


def show(data):
    results = data[COLUMNS_IN_SHOW]
    results = results.head(50)

    print('Here\'s your informations:')
    print(results)

