import csv
from enum import Enum
from functions.update import update_housing
from functions.add import add_housing
from functions.search import *


class Choice(Enum):
    SHOW = 1
    ADD = 2
    UPDATE = 3
    DELETE = 4
    EXIT = 5



print("="*5 + " Welcome to New York Housing Admin" + "="*5)
while True:
    print('')
    print("What do you wish to do?")
    print("\t1. Show housing data")
    print("\t2. Add new housing data")
    print("\t3. Update housing data")
    print("\t4. Delete housing data")
    print("\t5. Exit")

    choice_is_valid = False
    while not choice_is_valid:
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print('invalid choice.')
        else:
            choice_is_valid = True

    if (choice == Choice.SHOW.value):
        pass

    elif (choice == Choice.ADD.value):
        pass

    elif (choice == Choice.UPDATE.value):

        data_id = input('enter record ID : ')

        if (check_id_exists(data_id)):
            column_names = COLUMN_NAMES_BY_CATEGORY
            
            for column_category in column_names.keys():
                should_update = input(f'update {column_category}? (y/n) ')
                match should_update:
                    case 'y':
                        columns = column_names[column_category]

                        if (type(columns) == str):
                            column = columns
                            new_value = input(f'enter new value for {column} : ')
                            update_housing(data_id, column, new_value)

                        else:
                            for column in columns:
                                new_value = input(f'enter new value for {column} : ')
                                update_housing(data_id, column, new_value)

                    case 'n':
                        print(f'bypassing {column_category}')
                    
                    case _:
                        print('invalid choice, bypassing...')
        else:
            print('id not found.')


    elif (choice == Choice.DELETE.value):
        pass

    elif (choice == Choice.EXIT.value):
        exit(1)
    
    else:
        print('invalid choice.')
