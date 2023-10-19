import pandas as pd
from config import FILE_PATH

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def show(sorted_column, ascending):

    file_name = FILE_PATH
    data = pd.read_csv(file_name)
    
    selected_columns = ['id', 'name', 'host_name', 'price', 'availability_365']
    results = data[selected_columns]
    results.sort_values(by=sorted_column, ascending=ascending)
    results = results.head(50)

    print('Here\'s your informations:')
    print(results)
    