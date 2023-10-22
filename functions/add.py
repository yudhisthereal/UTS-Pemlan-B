import csv
import random
import pandas as pd
from config import FILE_PATH

df = pd.read_csv(FILE_PATH)

def last_id():
    return df['id'].max()

def add_housing(name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights):
    id = last_id() + random.randint(1,1000)
    with open(FILE_PATH, mode='a', newline='') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerow([id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,None,None,None,None,None])