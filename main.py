import csv
import pandas as pd
from enum import Enum
from functions.custom_input import *

from menu_interractions import *

df = pd.read_csv(FILE_PATH)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class Choice(Enum):
    HELP = 0
    SHOW = 1
    SEARCH = 2
    ADD = 3
    UPDATE = 4
    DELETE = 5
    EXIT = 6


def show_help():
    print("""1. Show 
          This function is used to display housing in order. sorting can 
          be done by id, name, host name, price, and availability 
          for a year.""")
    print("""2. Search
          This function is used to search for lodging based on 
          id, name, host, neighborhood, price, and minimum nights. 
          It will display all housing that matches the search.""")
    print("""3. Add 
          This function is used to add new housing data to the database. 
          It will ask for important data that must be added, 
          such as housing name, host id, host name, etc.""")
    print("""4. Update 
          This function is used to update housing data in the database. 
          It will ask if you want to update the data. 
          Press 'y' for yes and 'n' for no.""")
    print("""5. Delete 
          This function is used to delete housing data in the database. 
          It will ask which housing ID that want to be deleted.""")



print("="*5 + " Welcome to New York Housing Admin" + "="*5)
while True:
    print('')
    print("What do you wish to do?")
    print("0. Show help")
    print("1. Show housing data")
    print("2. Search for housing data")
    print("3. Add new housing data")
    print("4. Update housing data")
    print("5. Delete housing data")
    print("6. Exit")

    choice = int_input('enter your choice : ')
    choice = int(choice)

    if (choice == Choice.HELP.value):
        show_help()
    
    elif (choice == Choice.SHOW.value):
        menu_show(df)

    elif (choice == Choice.SEARCH.value):
        menu_search(df)

    elif (choice == Choice.ADD.value):
        menu_add(df)

    elif (choice == Choice.UPDATE.value):
        menu_update()

    elif (choice == Choice.DELETE.value):
        menu_delete(df)

    elif (choice == Choice.EXIT.value):
        exit(1)

    else:
        print('invalid choice.')
