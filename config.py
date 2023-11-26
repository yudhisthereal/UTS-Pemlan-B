FILE_PATH = "AB_NYC_2019.csv"
TEMP_FOLDER = "temp"
TEMP_PATH = None


COLUMNS_IN_SHOW = ['id', 'name', 'host_name', 'neighbourhood', 'price']
WIDTHS_IN_SHOW = (5, 50, 15, 25, 5)

COLUMNS_IN_SEARCH = ['id', 'name', 'neighbourhood',
                     'room_type', 'price', 'minimum_nights', 'availability_365']
WIDTHS_IN_SEARCH = (5, 45, 25, 10, 5, 5, 5)


def set_temp_path(path):
    global TEMP_PATH
    TEMP_PATH = path


def get_temp_path():
    return TEMP_PATH

