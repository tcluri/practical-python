# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filestream, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a delimiter separated file object into a list of records
    '''
    if type(filestream) == str:
        raise TypeError('The input should be a TextIOWrapper class and not a string')
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = [each_fileobject.split(delimiter) for each_fileobject in filestream]
    # with open(filename) as f:
    #     rows = csv.reader(f, delimiter=delimiter)


    # Indices of the select columns
    indices = []
    # Check if the headers are present
    if has_headers:
        # Read the file headers
        headers = [elem.strip() for elem in rows[0]]
        rows = rows[1:]
        # Select only desired columns
        if select:
            indices = [headers.index(select_ind) for select_ind in select]
            headers = select
    # Build the output for records
    records = []
    for row_ind, row in enumerate(rows, start=1):
        if not row:    # Skip rows with no data
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {row_ind}: Couldn't convert {row}")
                    print(f"Row {row_ind}: Reason", e)
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
