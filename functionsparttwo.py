def contains_purple(*args):
  if "purple" in args:
    return True
  return False


# s

def combine_words(word, **kwargs):
  if "suffix" in kwargs:
    return word + kwargs["suffix"]
  elif "prefix" in kwargs:
    return kwargs["prefix"] + word
  else:
    return word

# print(combine_words(" Mister", prefix = "Mrs"))


'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(**kwargs):
    result = None
    num1 = kwargs["first"]
    num2 = kwargs["second"]
    if kwargs["operation"] == "add":
        result = num1 + num2
    elif kwargs["operation"] == "subtract":
        result = num1 - num2
    elif kwargs["operation"] == "multiply":
        result = num1 * num2
    elif kwargs["operation"] == "divide":
        result = num1 / num2
    if kwargs["make_float"]:
        result = float(result)
    else:
        result = int(result)
    if "message" in kwargs:
        return "{} {}".format(kwargs["message"],result)
    else:
        return "The result is {}".format(result)


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final


def decrement_list(list1):
    return list(map(lambda x: x-1, list1))



def is_containing_strings(listing):
  return all(isinstance(s, str) for s in listing)

# print(is_containing_strings(["dunlop", 3,"tests","hello"]))

# define sum_even_values
def sum_even_values(*args):
    if all(s % 2 != 0 for s in args):
        return 0
    return sum(s for s in args if s % 2 == 0)


def sum_floats(*args):
    floats = (f for f in args if type(f) == float)
    return sum(floats)


def interleave(str1,str2):
  zipped = list(zip(str1,str2))
  result = ''
  zipped2 = [''.join(z) for z in zipped]
  print(zipped2)
  result = ''.join(zipped2)
  return result

# print(interleave("hi","ha"))

def triple_and_filter(nums):
    nums=list(filter(lambda n: n % 4 == 0, nums))
    return [n*3 for n in nums]
print(triple_and_filter([1,2,3,4]))