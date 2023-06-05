"""
- variable declaration
- log statement
- type check
- length check
- comment
    - single line
    - multiline
- Data Types
    - Primitive
        - Boolean
        - Numbers
        - Strings
    - Composite
        - List 
            - initialize
            - access value
            - change value
            - add value
            - delete value
        - Tuples
            - initialize
            - access value
            - change value
            - add value
            - delete value
        - Dictionary
            - initialize
            - access value
            - change value
            - add value
            - delete value
- conditional
    - if
    - else if
    - else
- for loop
    - start
    - stop
    - increment
    - break
    - continue
    - sequence
- while loop
    - start
    - stop
    - increment
- function
    - parameter
    - argument
    - return

* Bonus: Errors

- NameError: name <variable name> is not defined
- TypeError: 'tuple' object does not support item assignment
- KeyError: 'favorite_team'
- IndexError: list index out of range
- IndentationError: unexpected indent
- AttributeError: 'tuple' object has no attribute 'pop'
- AttributeError: 'tuple' object has no attribute 'append'
- Tuples
    - change value
    - add value
    - delete value
"""

num1 = 42  # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # Boolean
string = 'Hello World'  # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage',
                  'Jalepenos', 'Cheese', 'Olives']  # List
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Dictionary
fruit = ('blueberry', 'strawberry', 'banana')  # Tuples
print(type(fruit))  # type check
print(pizza_toppings[1])  # log statement
pizza_toppings.append('Mushrooms')  # add value
print(person['name'])  # access value
person['name'] = 'George'  # change value
person['eye_color'] = 'blue'  # add value
print(fruit[2])  # access value


# if else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


# for loop
for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
while (x < 5):
    print(x)
    x += 1

pizza_toppings.pop()  # delete value
pizza_toppings.pop(1)  # delete value

print(person)  # log statement
person.pop('eye_color')  # delete value
print(person)  # log statement


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


# function
print_hello_ten_times()


# function parameter
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
