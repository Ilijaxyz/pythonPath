#Learning experience of strings operations

x = 100
dragons = 1
#print(dragons + x)

cash = 599888333.44
#print(cash/5)

''' Variable nameing convention letter or underscore to start the name '''
''' Use snake_case '''
''' ALL caps for constants '''


''' Dynamic typing showcase '''
awesome = True
#print(awesome)

awesome = "a dog"
#print(awesome)

awesome = None # Concept of nothing in Pyton
#print(awesome)

awesome = 22 / 7
#print(awesome)

'''Escape characters all start with backslash'''
''' \n new line'''

message = "he said \"hey\""
#print(message)

mountain = "/\\"
#print(mountain)

''' Formating strings '''
''' Interpolation and F strings there is also .format method'''
lucky_number = 10
msg = f"my {lucky_number}"
#print(msg)

decimal = 2.3434322
integer = int(decimal) # it dosen't round just chops off decimal numbers
print(integer)

numbers = [2, 3, 4]
number_string = str(numbers)
print(number_string)