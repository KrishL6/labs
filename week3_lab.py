# This code prints numbers from 1 to 10 using a for loop

"""
for index in range(2, 21, 2):
    print (index)
"""

costs = [15.00, 12.50, 3.75, 40.25, 6.99]

total_cost = 0

for index in range(len(costs)):
    total_cost += costs[index]

text = f"The total cost is: {total_cost:.2f}"
print(text)