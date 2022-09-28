# pcost.py
#
# Exercise 1.33 Reading from command line
import sys
import csv
from report import read_portfolio

def portfolio_cost(filename):
   portfolio = read_portfolio(filename)
   return portfolio.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    print(f"Total cost: {portfolio_cost(args[1])}")


if __name__ == '__main__':
    import sys
    main(sys.argv)
