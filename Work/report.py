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
            if row == []:
                continue
            prices_dictionary[row[0]] = float(row[1])
    return prices_dictionary


# Ex 2.7 - Finding out if you can retire
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_gain_or_loss = 0

for company_shares in portfolio:
    company_name = company_shares['name']
    share_price = company_shares['price']
    num_shares = company_shares['shares']

    total_gain_or_loss += (share_price - prices[company_name]) * num_shares

if total_gain_or_loss > 0:
    print(f"Profit of {round(total_gain_or_loss, 2)}")
else:
    print(f"Loss of {round(total_gain_or_loss, 2)}")
