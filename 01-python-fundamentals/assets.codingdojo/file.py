# variable declaration
# Data Types
# Numbers
num1 = 42
num2 = 2.3
# Boolean
boolean = True
# Strings
string = 'Hello World'
# List 
# initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
# log statement
#---- type check
print(type(fruit))
# sequence
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# conditional
# if
if num1 > 45:
    print("It's greater")
# else
else:
    print("It's lower")
# if
if len(string) < 5:
    print("It's a short word!")
# else if
# --length check
elif len(string) > 15:
    print("It's a long word!")
# else
else:
    print("Just right!")
# for loop
# ------------STOP
for x in range(5):
    print(x)
# for loop
# ---------START--STOP
for x in range(2, 5):
    print(x)
# for loop
# ----------START-STOP-STEP
for x in range(2, 10,  3):
    print(x)
# while loop
# start
x = 0
# ----STOP--
while(x < 5):
    print(x)
    # increment
    x += 1

# delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

# for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

# --------------------parameter
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

# ----------------------------parameter
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

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
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)