# report.py
#
# Exercise 2.5 - List of dictionaries
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    # portfolio = []
    return parse_csv(filename, types=[str, int, float], silence_errors=True)

    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row_num, row in enumerate(rows, start=1):
    #         # holding_dict = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
    #         row = (row[0], int(row[1]), float(row[2]))
    #         holding_dict = dict(zip(headers, row))
    #         portfolio.append(holding_dict)
    # return portfolio


# portfolio = read_portfolio('Data/portfolio.csv')

# from pprint import pprint
# pprint(portfolio)

def read_prices(filename):
    return dict(parse_csv(filename, types=[str, float], has_headers=False, silence_errors=True))
    # prices_dictionary = {}
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         if row == []:
    #             continue
    #         prices_dictionary[row[0]] = float(row[1])
    # return prices_dictionary


def make_report(portfolio, prices):
    report = []
    for company in portfolio:
        company_name = company['name']
        company_num_shares = company['shares']
        company_price = company['price']
        price_company = prices[company_name]
        company_price_change = price_company - company_price
        company_tuple = (company_name, company_num_shares, price_company, company_price_change)
        report.append(company_tuple)
    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    # Align and print the headers and the next line
    print('%10s %10s %10s %10s' % headers)
    print(10*'-', 10*'-', 10*'-', 10*'-')
    for name, shares, price, change in report:
            print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10s} {change:>10.2f}')


def portfolio_report(portfolio_file, prices_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
