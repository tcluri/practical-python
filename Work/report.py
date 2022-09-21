# report.py
#
# Exercise 2.5 - List of dictionaries
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding_dict = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding_dict)
    return portfolio


# portfolio = read_portfolio('Data/portfolio.csv')

# from pprint import pprint
# pprint(portfolio)

def read_prices(filename):
    prices_dictionary = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices_dictionary[row[0]] = float(row[1])
            except IndexError:
                print("There is no data in the row.")
    return prices_dictionary
