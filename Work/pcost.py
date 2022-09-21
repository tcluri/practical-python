# pcost.py
#
# Exercise 1.31

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as stocks_file:
        headers = next(stocks_file).split(',')
        # For each stock calculate the total cost
        for each_company_line in stocks_file:
            each_company_list = each_company_line.split(',')
            try:
                num_shares = int(each_company_list[1])
            except ValueError:
                print(f"Warning! There are no shares for {each_company_list[0]}")
                continue
            total_cost += num_shares * float(each_company_list[2].strip())
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f"Total cost: {cost}")
