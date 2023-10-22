import csv
from config import *


def update_housing(id, column_name, new_value) -> int:
    """
    Update a data in NYC Housing Dataset csv file.

    :param id: The ID of the record to update.
    :type id: int or str

    :param column_name: The name of the column to update.
    :type column_name: str

    :param new_value: The new value to set in the specified column.
    :type new_value: str

    :return: Returns 1 if the update is successful, 0 if the record is not found.
    :rtype: int
    """

    data_updated = False
    rows = []

    with open(get_temp_path(), 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row['id'] == str(id):
                row[column_name] = str(new_value)
                data_updated = True
            rows.append(row)

        if data_updated:
            with open(get_temp_path(), mode='w', newline='', encoding='utf-8') as file:
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(rows)
            return 1
        return 0
