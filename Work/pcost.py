# pcost.py
#
# Exercise 1.27
total_cost = 0
with open('Data/portfolio.csv', 'rt') as stocks_file:
    headers = next(stocks_file).split(',')
    # For each stock calculate the total cost
    for each_company_line in stocks_file:
        each_company_list = each_company_line.split(',')
        total_cost += int(each_company_list[1]) * float(each_company_list[2].strip())
print(f"Total cost {total_cost}")
