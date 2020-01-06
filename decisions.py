''' Decisons in python '''
from random import randint

# color = input("What is your favourite color?\n")


# if color == 'red':
#   print(f"Nice, your favourite color is {color}.")
# elif color == 'blue':
#   print(f"Yayy, your favourite color is {color}.")
# else:
#   print(f"Your favourite color is {color}.")

choice = randint(1,10) #random int in range of 1 to 10

# if choice == 7:
#   print("lucky")
# else:
#   print("unlucky")

''' Truthiness '''
# x = 1
# y = 1
# if x is y:
#   print("we used is as a comparison operator")


''' Naturally falsy are EMPTY OBJECTS, EMPTY STRINGS, NONE, ZERO '''
some_value = ""
if some_value:
  print("will not print because empty string it's falsy")

if 0:
  print("this also will not execute because zero is falsy")


''' Multi line comments
Logical operators combined with comparison operators
'''

# city = input("Where do you live? ")
# if city == "Los Angeles" or city == "San Francisco":
#   print("Yay California")
# else:
#   print("Nope")

# if 1 < -1 or 10 > 2:
#   print("logical or")

# age = 23
# if not ((age > 2 and age < 10) or age >= 65):
#   print("You are not a senior or a child ticket price is 10 dollars")
# else:
#   print("You are child or senior ticket price is 2 dollars")

