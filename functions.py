'''
FUNCTIONS

useful for DRY
box of code
organize things
'''


# def say_hi():
#   print("Hi")

# say_hi()

def print_squer(value):
  return value**2

result = print_squer(4)
# print(result)

total = 0


def increment():
  """ A simple function that increments a value"""
  global total
  total += 1
  return total

# print(increment())

# print(increment.__doc__)


''' 
Documenting a function with triple quotation marks
Must be first line under the function 
it is accessable via <name_of_the_function>.__doc__
'''

def number_compare(first_num,second_num):
    if first_num == second_num:
        return "Numbers are equal"
    elif second_num > first_num:
        return "Second is greater"
    return "First is greater"

def single_letter_count(word, letter):
    letter = letter.lower()
    word = word.lower()
    if letter in word:
        return word.count(letter)
    return 0

# print(single_letter_count("heLLo", ""))

# flesh out multiple_letter count:
def multiple_letter_count(word):
    return { s : word.count(s) for s in word}


'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list1, command, location, value = 20):
    if(command.lower() == "remove" and location.lower() == "end"):
        return list1.pop()
    elif(command.lower() == "remove" and location.lower() == "beginning"):
        return list1.pop(0)
    elif(command.lower() == "add" and location.lower() == "beginning"):
        list1.insert(0, value)
        return list1
    list1.append(value)
    return list1

def is_palindrome(expression):
    expression = expression.lower()
    print(expression)
    expression = expression.replace(" ","")
    print(expression)
    backwards = list(expression)
    print(backwards)
    backwards.reverse()
    print(backwards)
    expression = list(expression)
    print(expression)
    if(backwards == expression):
        return True
    return False
    

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

print(is_palindrome("a man apele panama"))


def capitalize(string):
    return string[:1].upper() + string[1:]

# thruty list
def compact(list1):
    thruty_list = []
    for i in list1:
        if(i):
            thruty_list.append(i)
    return thruty_list


# flesh out intersection pleaseeeee
def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    result = set1 & set2 
    return list(result)

def intersection(l1, l2):
    return [val for val in l1 if val in l2]

def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

def partition(list1, fn):
   thruty = []
   falsy = []
   for v in list1:
      if(fn(v)):
         thruty.append(v)
      else:
         falsy.append(v)
   return [thruty,falsy]