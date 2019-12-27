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

if choice == 7:
  print("lucky")
else:
  print("unlucky")

