# pcost.py
#
# Exercise 1.33 Reading from command line
import sys
import csv
from report import read_portfolio

def portfolio_cost(filename):
   return sum([each_company['shares'] * each_company['price']
                for each_company in read_portfolio(filename)])


def main(argv):
    print(f"Total cost: {portfolio_cost(argv[1])}")


if __name__ == '__main__':
    import sys
    if sys.argv[0] == 'pcost.py':
        main(sys.argv)
