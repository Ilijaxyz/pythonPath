''' let's do lists
    data structure -> store other data in a structured way
'''
# task = ["Install Python", "Learn Python", "Take a break"]
#task = None

# print(len(task))

# new_list = list(range(1,10)) # range to a list

# print(new_list)

# friends = ["Tara", "Mara", "Vara"]

# for name in range(len(friends)):
#   print(friends[name])

# we can go backwards but start is -1

# if ("Tara" in friends):
#   print("It's cool")

# for friend in friends:
#   print(friend)

# i = 0
# while i < len(friends):
#   print(friends[i])
#   i += 1

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# result = ""

# for sound in sounds:
#     result += sound.upper()

# print(result)
# append extend insert

# sounds.insert(0, "HELLO") # add on first postion in list
# print(sounds)

''' Slicing copyis of lists giv me part form index 3 to 5 it is not a metod we use squer brackets
some_list[start:end:step] makes a unique copy, IT IS EXCLUSIVE(does not include the end point)
'''
'''
LIST COMPREHENSION 
'''

# nums = [1, 2, 3]
# new_nums = [x * 10 for x in nums]

# print(f"OLD {nums}")
# print(f"NEW {new_nums}")

# list1 = ["Elie", "Tim", "Matt"]

# answer = [name[0] for name in names]

# list2 = [1,2,3,4,5,6]

# answer2 = [num for num in numbers if num % 2 = 0]


# print(f" {answer} \n {answer2}")

numbers = list(range(1,101))
numbers = [num for num in numbers if num % 12 == 0]

answer = [value for value in "amazing" if value not in "aeiou"]

answer2 = [[x for x in range(3)] for i in range(3)]

print(answer)
print(answer2)