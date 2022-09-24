# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)


        # Read the file headers
        headers = next(rows)
        # Select only desired columns
        if select:
            indices = [headers.index(select_ind) for select_ind in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            record = dict(zip(headers, row))
            records.append(record)

    return records
