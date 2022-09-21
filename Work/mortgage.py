# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
init_extra_months = 12
months_payed = 0

while principal > 0:
    if init_extra_months > 0:
        extra_payments = 1e3
    else:
        extra_payments = 0
    init_extra_months -= 1
    months_payed += 1
    principal = (principal * (1+rate/12)) - (payment + extra_payments)
    total_paid = total_paid + payment + extra_payments

print('Total paid', round(total_paid, 2))
print('Months payed', round(months_payed, 2))
