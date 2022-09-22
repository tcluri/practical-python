# pcost.py
#
# Exercise 1.33 Reading from command line
import sys
import csv

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as stocks_file:
        rows = csv.reader(stocks_file)
        headers = next(rows)
        # For each stock calculate the total cost
        for row_num, each_company_row in enumerate(rows, start=1):
            record = dict(zip(headers, each_company_row))
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += num_shares * price
            except ValueError:
                print(f'Row {row_num}: Bad row: {each_company_row}')
                # print(f"Warning! There are no shares for {each_company_row[0]}")
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")

# cost = portfolio_cost('Data/portfolio.csv')
# print(f"Total cost: {cost}")

# # Test with missing file
# cost_with_missing_shares = portfolio_cost('Data/missing.csv')
# print(f"Cost for Data/missing.csv {cost_with_missing_shares}")
