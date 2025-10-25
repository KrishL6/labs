# This code prints numbers from 1 to 10 using a for loop

"""
for index in range(2, 21, 2):
    print (index)
"""

# This code calculates the total cost from a list of costs

"""
costs = [15.00, 12.50, 3.75, 40.25, 6.99]

total_cost = 0

for index in range(len(costs)):
    total_cost += costs[index]

text = f"The total cost is: {total_cost:.2f}"
print(text)
"""
"""
# code that prints a 5x5 square of asterisks (*)

for index in range(5):
    print()
    for index in range(5):
        print('*', end=' ')
"""

"""
# code that prints a right-angled triangle of asterisks (*)

for index in range (6):
    print()
    for j in range (index):
        print('*', end=' ')
"""

#code fore quitting loop by user input

user_input = ""

while True:
    print("---- calcualtor menu ----")
    user_input = input("a - add, s - subtract, q - quit: ")
    if user_input == "q":
        print("quitting the program")
        break
    elif user_input == "a":
        print("you chose addition")
    elif user_input == "s":
        print("you chose subtraction")
    else:
        print("invalid input, please try again")

print("program ended")

