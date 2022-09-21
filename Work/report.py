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


# Ex 2.7 - Finding out if you can retire
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# total_gain_or_loss = 0

# for company_shares in portfolio:
#     company_name = company_shares['name']
#     share_price = company_shares['price']
#     num_shares = company_shares['shares']

#     total_gain_or_loss += (prices[company_name] - share_price) * num_shares

# if total_gain_or_loss > 0:
#     print(f"Profit of {round(total_gain_or_loss, 2)}")
# else:
#     print(f"Loss of {round(total_gain_or_loss, 2)}")

report = make_report(portfolio, prices)
for r in report:
    print(r)
