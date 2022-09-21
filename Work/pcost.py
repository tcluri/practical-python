# pcost.py
#
# Exercise 1.32
import csv

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as stocks_file:
        rows = csv.reader(stocks_file)
        headers = next(rows)
        # For each stock calculate the total cost
        for each_company_row in rows:
            try:
                num_shares = int(each_company_row[1])
            except ValueError:
                print(f"Warning! There are no shares for {each_company_row[0]}")
                continue
            total_cost += num_shares * float(each_company_row[2])
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f"Total cost: {cost}")

# Test with missing file
cost_with_missing_shares = portfolio_cost('Data/missing.csv')
print(f"Cost for Data/missing.csv {cost_with_missing_shares}")
