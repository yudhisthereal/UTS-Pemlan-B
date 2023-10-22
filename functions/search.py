import csv
from config import *

def check_id_exists(target_id) -> bool:
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(target_id):
                return True
    return False