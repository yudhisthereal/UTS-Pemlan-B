from time import sleep
from functions.show import *
from functions.search import *
from functions.custom_input import *
from functions.delete import *
from functions.add import *
from functions.update import *
from config import COLUMNS_IN_SHOW, COLUMNS_IN_SEARCH

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

def menu_show(data):
    show(data)

    # Ask if the user wants to apply filters
    apply_filter = yesno_input('Do you want to filter the data? (y/n) ')

    while apply_filter == 'y':

        print("""Columns' indices
        1. Housing ID
        2. Housing Name
        3. Host Name
        4. Neighbourhood
        5. Price
        """)
        sort_by = int(int_input('Sort by which column? (1/2/3/4/5) '))
        sort_by -= 1
        while sort_by not in range(5):
            print('Your choice must be one of (1/2/3/4/5)')
            sort_by = int(int_input('Sort by which column? (1/2/3/4/5) '))
            sort_by -= 1

        ascending = True if yesno_input(
            'sort ascending? (y/n) ') == 'y' else False

        show_filtered(data, COLUMNS_IN_SHOW[sort_by], ascending)

        print()
        apply_filter = yesno_input('Do you want to re-filter the data? (y/n) ')

    print('Alrighty!')
    sleep(0.5)


def menu_search(df):

    searching = True
    while searching:

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

        if (search_by not in [0, 4, 5]):  # if query shouldn't be numbers
            query = input('Enter query : ')
        else:
            query = int_input('Enter query : ')
        results = search(df, query, COLUMNS_IN_SEARCH[search_by])

        results = results.head(25) if search_by != 0 else results

        rows_in_results = results.shape[0]
        if rows_in_results > 0:
            print('Here\'s what we found : ')
            print(results)
        else:
            print('housing not found.')
            sleep(0.5)

        print()
        searching = True if yesno_input(
            'search again? (y/n) ') == 'y' else False

    print('Alrighty!')
    sleep(0.5)


def menu_add(df):

    adding = True
    while adding:

        name = input('enter housing name : ').strip()
        host_id = int_input('enter host id : ')

        host_name = input('enter host name : ').strip()
        neighbourhood_group = input('enter neighbourhood group : ').strip()
        neighbourhood = input('enter neighbourhood : ').strip()

        latitude = float_input('enter latitude : ')
        longitude = float_input('enter longitude : ')

        room_type = input('enter room type : ').strip()
        price = int_input('enter price : ').strip()
        minimum_nights = int_input('enter minimum nights : ').strip()
        availability = int_input('enter availability : ').strip()

        add_housing(df, name, host_id, host_name, neighbourhood_group,
                    neighbourhood, latitude, longitude, room_type, price, minimum_nights, availability)

        print()
        print(f'"{name}" added successfully!')
        sleep(0.5)
        print()
        adding = True if yesno_input(
            'add another housing data? (y/n) ') == 'y' else False

    print('Alrighty!')
    sleep(0.5)


def menu_update():

    updating = True
    while updating:

        data_id = input('enter housing ID : ')

        if (id_exists(data_id)):
            column_names = COLUMN_NAMES_BY_CATEGORY

            for column_category in column_names.keys():
                should_update = yesno_input(
                    f'update {column_category}? (y/n) ')
                match should_update:
                    case 'y':
                        columns = column_names[column_category]

                        if (type(columns) == str):
                            column = columns
                            if column in ('latitude', 'longitude'):
                                new_value = float_input(
                                    f'enter new value for {column} : ')
                            elif column in ('price', 'minimum_nights', 'availability_365'):
                                new_value = int_input(
                                    f'enter new value for {column} : ')
                            else:
                                new_value = input(
                                    f'Enter new value for {column} :')

                            print(f'updating {column} to {new_value}...')

                            update_success = update_housing(
                                data_id, column, new_value)

                            if update_success:
                                print(f'"{column}" updated')
                            else:
                                print(f'"{column}" was not updated')

                            sleep(0.5)

                        else:
                            for column in columns:
                                if column in ('latitude', 'longitude'):
                                    new_value = float_input(
                                        f'enter new value for {column} : ')
                                elif column in ('price', 'minimum_nights', 'availability_365', 'host_id'):
                                    new_value = int_input(
                                        f'enter new value for {column} : ')
                                else:
                                    new_value = input(
                                        f'Enter new value for {column} :')


                                print(f'updating {column} to {new_value}...')

                                update_success = update_housing(
                                    data_id, column, new_value)
                                if update_success:
                                    print(f'"{column}" updated')
                                else:
                                    print(f'"{column}" was not updated')

                                sleep(0.5)

                    case 'n':
                        print(f'bypassing {column_category}')
                    case _:
                        print('invalid choice, bypassing...')

                sleep(0.5)

        else:
            print('id not found.')
            sleep(0.5)

        print()
        updating = True if yesno_input(
            'update another? (y/n)') == 'y' else False

    print('Alrighty!')
    sleep(0.5)


def menu_delete(df):

    deleting = True
    while deleting:

        housing_id = int(int_input('Enter housing ID : '))
        if (id_exists(housing_id)):
            to_be_deleted = search(df, str(housing_id), 'id')
            print('housing to be deleted:')
            print(to_be_deleted)

            proceed_deletion = True if yesno_input(
                'Confirm deletion (y/n) ') == 'y' else False
            if proceed_deletion:
                delete_housing(df, housing_id)
                print('Deletion successful')
                sleep(0.5)
        else:
            print('id not found')
            sleep(0.5)

        print()
        deleting = True if yesno_input(
            'delete another? (y/n)') == 'y' else False

    print('Alrighty!')
    sleep(0.5)
