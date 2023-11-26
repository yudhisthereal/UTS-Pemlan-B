from time import sleep
from functions.show import *
from functions.search import *
from functions.custom_input import *
from functions.delete import *
from functions.add import *
from functions.update import *
from config import COLUMNS_IN_SHOW, COLUMNS_IN_SEARCH




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
