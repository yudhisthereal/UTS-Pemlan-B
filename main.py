import csv
import pandas as pd
from enum import Enum
from functions.update import update_housing
from functions.show import show
from functions.add import add_housing
from functions.search import *
from functions.delete import delete_housing


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class Choice(Enum):
    SHOW = 1
    SEARCH = 2
    ADD = 3
    UPDATE = 4
    DELETE = 5
    EXIT = 6


def int_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        try:
            result = int(input(message).strip())
        except ValueError:
            print('your input must be a number')
        else:
            input_is_valid = True
    
    return str(result)


def float_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        try:
            result = float(input(message).strip())
        except ValueError:
            print('input must be a real number (e.g. 123.4567)')
        else:
            input_is_valid = True
    
    return str(result)


print("="*5 + " Welcome to New York Housing Admin" + "="*5)
while True:
    print('')
    print("What do you wish to do?")
    print("1. Show housing data")
    print("2. Search for housing data")
    print("3. Add new housing data")
    print("4. Update housing data")
    print("5. Delete housing data")
    print("6. Exit")

    choice = int_input('enter your choice : ')
    choice = int(choice)

    if (choice == Choice.SHOW.value):
        columns = ['id', 'name', 'host_name', 'price', 'availability_365']
        print('Sort results by')
        for i, column in enumerate(columns):
            column = column.replace('-', ' ')
            print(f'{i+1}. {column}')

        sort_by = int_input('sort by (1/2/3/4/5)')
        while sort_by not in ('1', '2', '3', '4', '5'):
            print('please select from (1/2/3/4/5).')
            sort_by = int_input('sort by (1/2/3/4/5)')
        sort_by = int(sort_by) - 1
        
        sorted_column = columns[sort_by]
        
        input_is_valid = False
        ascending = False
        while not input_is_valid:
            ascending = input('sort ascending? (y/n) ')
            match ascending:
                case 'y':
                    ascending = True
                    input_is_valid = True
                case 'n':
                    ascending = False
                    input_is_valid = True
                case _:
                    input_is_valid = False
                    print('Input must one of (y/n)')
                

        show(sorted_column, ascending)

    elif (choice == Choice.SEARCH.value):
        column_names = ('id', 'name', 'host_name', 'neighbourhood', 'price', 'minimum_nights')

        print('What do you want to search by?')
        print('0. Housing ID')
        print('1. Housing name')
        print('2. Housing host')
        print('3. Neighborhood')
        print('4. Price')
        print('5. Minimum Nights')
        
        search_by = int_input('Enter your choice (0/1/2/3/4/5) : ')
        while (search_by not in ['0', '1', '2', '3', '4', '5']):
            print('your choice must range from 0 to 5.')
            search_by = int_input('Enter your choice (0/1/2/3/4/5) : ')
        
        search_by = int(search_by)

        if (search_by not in [0, 4, 5]): # if query shouldn't be numbers
            query = input('Enter query : ')
        else:
            query = int_input('Enter query : ')
        results = search(query, column_names[search_by])

        results = results.head(25) if search_by != 0 else results

        rows_in_results = results.shape[0]
        if rows_in_results > 0:
            print('Here\'s what we found : ')
            print(results)
        else:
            print('housing not found.')

    elif (choice == Choice.ADD.value):
        name = input('enter housing name : ').strip()

        host_id = int_input('enter host id : ')

        host_name = input('enter host name : ').strip()
        neighbourhood_group = input('enter neighbourhood group : ').strip()
        neighbourhood = input('enter neighbourhood : ').strip()

        latitude = float_input('enter latitude : ')
        longitude = float_input('enter longitude : ')

        room_type = input('enter room type : ').strip()
        price = input('enter price : ').strip()
        minimum_nights = input('enter minimum nights : ').strip()

        add_housing(name, host_id, host_name, neighbourhood_group,
                    neighbourhood, latitude, longitude, room_type, price, minimum_nights)
        
        print(f'the new housing, "{name}" and its information were added successfully')

    elif (choice == Choice.UPDATE.value):

        data_id = input('enter housing ID : ')

        if (id_exists(data_id)):
            column_names = COLUMN_NAMES_BY_CATEGORY

            for column_category in column_names.keys():
                should_update = input(f'update {column_category}? (y/n) ')
                match should_update:
                    case 'y':
                        columns = column_names[column_category]

                        if (type(columns) == str):
                            column = columns
                            new_value = input(f'enter new value for {column} : ')

                            print(f'updating {column} to {new_value}...')

                            update_success = update_housing(data_id, column, new_value)

                            if update_success:
                                print(f'"{column}" updated')
                            else:
                                print(f'"{column}" was not updated')

                        else:
                            for column in columns:
                                new_value = input(f'enter new value for {column} : ')
                                
                                print(f'updating {column} to {new_value}...')

                                update_success = update_housing(data_id, column, new_value)
                                if update_success:
                                    print(f'"{column}" updated')
                                else:
                                    print(f'"{column}" was not updated')


                    case 'n':
                        print(f'bypassing {column_category}')

                    case _:
                        print('invalid choice, bypassing...')
        else:
            print('id not found.')

    elif (choice == Choice.DELETE.value):
        housing_id = int(input('Enter housing ID : '))
        if (id_exists(housing_id)):
            delete_housing(housing_id)
            print('Deletion successful')
        else:
            print('id not found')

    elif (choice == Choice.EXIT.value):
        exit(1)

    else:
        print('invalid choice.')
