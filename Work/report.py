# report.py
#
# Exercise 2.5 - List of dictionaries
from fileparse import parse_csv
import stock
import tableformat


def read_portfolio(filename):
    """
    Read a stock portfolio file object into a list of dictionary
    with keys name, shares, and price.
    """
    with open(filename) as lines:
        portfolio = parse_csv(lines, types=[str, int, float], silence_errors=True)
        portfolio = [stock.Stock(each_dict['name'], each_dict['shares'], each_dict['price'])
                     for each_dict in portfolio]
        return portfolio


def read_prices(filename):
    """"
    Read a file object of price data into a dict mapping names
    to prices.
    """
    with open(filename) as lines:
        return dict(parse_csv(filename, types=[str, float], has_headers=False, silence_errors=True))


def make_report(portfolio, prices):
    report = []
    for company in portfolio:
        company_name = company.name
        company_num_shares = company.shares
        company_price = company.price
        price_company = prices[company_name]
        company_price_change = price_company - company_price
        company_tuple = (company_name, company_num_shares, price_company, company_price_change)
        report.append(company_tuple)
    return report


def print_report(report, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    # Align and print the headers and the next line
    # print('%10s %10s %10s %10s' % headers)
    # print(10*'-', 10*'-', 10*'-', 10*'-')
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'${price:.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
        # print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10s} {change:>10.2f}')


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    # formatter = tableformat.CSVTableFormatter()
    # formatter = tableformat.HTMLTableFormatter()
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) not in (3,4):
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    try:
        portfolio_report(args[1], args[2], args[3])
    except:
        portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
