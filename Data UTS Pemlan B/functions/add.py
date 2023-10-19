import csv
import csv
from config import FILE_PATH

def last_id(df):
    return df['id'].max()


def add_housing(df, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, availability):
    id = last_id(df) + random.randint(1, 1000)
    with open(FILE_PATH, mode='a', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerow([id, name, host_id, host_name, neighbourhood_group, neighbourhood,
                            latitude, longitude, room_type, price, minimum_nights, None, None, None, None, availability])


