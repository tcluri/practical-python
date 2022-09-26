# report.py
#
# Exercise 2.5 - List of dictionaries
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    return parse_csv(filename, types=[str, int, float], silence_errors=True)


def read_prices(filename):
    return dict(parse_csv(filename, types=[str, float], has_headers=False, silence_errors=True))


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



def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    if sys.argv[0] == 'report.py':
        main(sys.argv)
