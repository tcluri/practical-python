# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1e3
months_num = 0

while principal > 0:
    months_num += 1
    actual_payment = payment
    if extra_payment_start_month <= months_num <= extra_payment_end_month:
        actual_payment = payment + extra_payment
    principal = (principal * (1+rate/12)) - (actual_payment)
    total_paid = total_paid + actual_payment
    # print("Months", months_num)
    # print("Actual payment", actual_payment)


print('Total paid', round(total_paid, 2))
print('Months payed', round(months_num, 2))
