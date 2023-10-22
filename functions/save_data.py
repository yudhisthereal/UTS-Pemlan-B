import os
import shutil
from config import TEMP_FOLDER, FILE_PATH, set_temp_path, get_temp_path


__has_unsaved_changes = False


def create_temp():
    if os.path.exists(TEMP_FOLDER) == False:
        os.mkdir(TEMP_FOLDER)

    split_filename = FILE_PATH.split('.')
    temp_filename = split_filename[0] + '.temp'
    temp_path = os.path.join(TEMP_FOLDER, temp_filename)

    if os.path.exists(temp_path):
        set_temp_path(temp_path)
        global __has_unsaved_changes
        __has_unsaved_changes = True
        return

    shutil.copy(FILE_PATH, temp_path)
    set_temp_path(temp_path)


def save():
    split_filename = FILE_PATH.split('.')
    temp_file = split_filename[0] + '.temp'
    temp_path = os.path.join(TEMP_FOLDER, temp_file)

    shutil.copy(temp_path, FILE_PATH)

    global __has_unsaved_changes
    __has_unsaved_changes = False


def destroy_temp():
    if os.path.exists(get_temp_path()):
        os.remove(get_temp_path())

    set_temp_path(None)


def has_unsaved_changes(has=None):
    global __has_unsaved_changes
    if has == None:
        return __has_unsaved_changes
    else:
        __has_unsaved_changes = has
        return None