# mortgage.py
#
# Exercise 1.17
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1e3
month_num = 0

while principal > 0:
    month_num += 1
    actual_payment = payment
    if extra_payment_start_month <= month_num <= extra_payment_end_month:
        actual_payment = payment + extra_payment
    # Principal fraction to calculate no overpay
    principal_fraction = (principal * (1+rate/12))
    if actual_payment >= principal_fraction:
        actual_payment = principal_fraction
    principal = principal_fraction - (actual_payment)
    total_paid = total_paid + actual_payment
    print(f"{month_num:10} {total_paid:10.2f} {principal:10.2f}")
    # print(month_num, round(total_paid, 2), round(principal,2))

print(f"Total paid {total_paid:10.2f}")
print(f"Months {month_num:10}")
