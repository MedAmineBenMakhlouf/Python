# variable declaration
# Data Types
# Primitive
# Numbers
num1 = 42
num2 = 2.3
# Boolean
boolean = True
# Strings
string = 'Hello World'
# Composite
# List 
# initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Dictionary
# initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# Tuples
# initialize
fruit = ('blueberry', 'strawberry', 'banana')

# log statement
#---- type check
print(type(fruit))
# ----access value
print(pizza_toppings[1])
# add value
pizza_toppings.append('Mushrooms')
# log statement
# ____access value
print(person['name'])
# change value
person['name'] = 'George'
person['eye_color'] = 'blue'
# log statement
# ____access value
print(fruit[2])

# conditional
# if
if num1 > 45:
    # log statement
    print("It's greater")
# else
else:
    # log statement
    print("It's lower")
# if
if len(string) < 5:
    # log statement
    print("It's a short word!")
# else if
# --length check
elif len(string) > 15:
    # log statement
    print("It's a long word!")
# else
else:
    # log statement
    print("Just right!")
# for loop
# ------------STOP
for x in range(5):
    # log statement
    print(x)
# for loop
# ---------START--STOP
for x in range(2, 5):
    # log statement
    print(x)
# for loop
# ----------START-STOP-STEP
for x in range(2, 10,  3):
    # log statement
    print(x)
# while loop
# start
x = 0
# ----STOP--
while(x < 5):
    # log statement
    print(x)
    # increment
    x += 1

# delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

# log statement
print(person)
# delete value
person.pop('eye_color')
# log statement
print(person)

# for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    # log statement
    print('After 1st if statement')
    if topping == 'Olives':
        break
# function
def print_hello_ten_times():
    # for loop
    for num in range(10):
        # log statement
        print('Hello')

print_hello_ten_times()

# --------------------parameter
def print_hello_x_times(x):
    # for loop
    for num in range(x):
        # log statement
        print('Hello')

# log statement
print_hello_x_times(4)

# ----------------------------parameter
def print_hello_x_or_ten_times(x = 10):
    # for loop
    for num in range(x):
        # log statement
        print('Hello')

# log statement
print_hello_x_or_ten_times()
# ---------------------argument
print_hello_x_or_ten_times(4)

# comment

# multiline

"""
Bonus section
"""

# single line

# print(num3)
# num3 = 72
# change value
# fruit[0] = 'cranberry'
#  access Value
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# add value
# fruit.append('raspberry')
# delete value
# fruit.pop(1)