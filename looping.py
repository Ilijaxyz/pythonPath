''' Let's go loooping
Collection of data to loop over
for idea is for every piece in the collection
'''
'''
iterable object is an collection of data
'''
# for letter in "hello":
#   print(letter)

# for number in range(1,8):
#   print(number)

# add all odd numbers from 10 to 20 inclusive
# x = 0
# for i in range(11,21,2):
#   x = x + i
# print(f"Sum of all odd nubmers from 10 to 20 inclusive is {x}")

# alternative solution
# x = 0
# for i in range(10,21):
#   if i % 2 != 0:
#     x = x + i
# print(f"sum is {x}")

# times = input("How many times do I have to tell you? ")
# times = int(times)

# for t in range(times):
#   print("Yup yup hello")

# for i in range(1,21):
#   if i % 2 != 0:
#     if i == 13: 
#       print(f"{i} is unlucky")
#     else:
#       print(f"{i} is odd")
#   else:
#     if i == 4: #chinese culture
#       print(f"{i} is unlucky")
#     else:
#       print(f"{i} is even")


# alternative solution to unlucky numbers small refatoring

# for i in range(1,21):
#   if i == 4 or i == 13:
#     state = "unlucky"
#   elif i % 2 == 0:
#     state = "even"
#   else:
#     state = "odd"
#   print(f"{i} is {state}")

''' WHILE LOOP distant cousin of if statement '''

# message = input("What is the password? ")
# password = "tomato"

# while message != password:
#   message = input("Nope, try again\n")

# print("YES YOU ARE IN!\n" * 10)

# for i in range(1,10):
#   print("\U0001F600" * i)

# print("---------SEPARATION------------" * 4)
# num = 1
# times_separation = 10
# while num < 20 and times_separation > 0:
#   print(times_separation * " " + "\U0001F600" * num)
#   num += 2
#   times_separation -= 1

''' Copying me game
'''

# stop_message = "stop copying me"

# print("Hey how it's going?")
# message = input()

# while message != stop_message:
#   print(f"{message}")
#   message = input()

# print("UGH Fine you win")

# i = 0
# while i <= 5:
#   i += 1
#   print(i)