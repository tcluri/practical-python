# bounce.py
#
# Exercise 1.5
init_height = 100
bounce_height = 3/5
bounces = 10
rounding_decimals = 4
for i in range(bounces):
    next_height = init_height * bounce_height
    print(i+1, round(next_height, rounding_decimals))
    init_height = next_height
