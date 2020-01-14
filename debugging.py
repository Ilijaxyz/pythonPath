'''
Common errors

Syntax error
def first: #syntax error
None = 1
return

Name error
nonexistent variable(is not defined)

Type error
len(5)
3 + "s"
len(2.66)

Index error
access invalid index

Value error
right type but not valid value
int('f')
int(['tr'])

KeyError for dictionary

AttributeError
"awesome".foo()
[1,2,3].hello()
'''

# raise ValueError("Invalid value")
import pdb

def colorize(text, color):
  pdb.set_trace()
  colors = ("yellow", "blue", "red")
  if type(text) is not str:
    raise TypeError("text must be instance of str")
  if type(color) is not str:
    raise TypeError("color must be instance of str")
  if color not in colors:
    raise ValueError("Invalid color")
  print(f"Printed {text} in {color}")

# colorize("hello", "red")
# colorize("ttt", "yellow")

'''Handle errors'''
try:
  colorize("","")
except: # never catch generic error handles all error
  print("Problem")

''' usually we dont keep pdb in code and is used like imort pdb; pdb.set_trace()'''





