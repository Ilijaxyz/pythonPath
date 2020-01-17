'''
OOP
encapsulate code
orginize code in calsses
'''

# class User:
  # pass # Ok I am done nothing to do here


class User:
  def __init__(self, first, last):
    self.first = first
    self.last = last

user = User("Joe","Satriani")
user2 = User("Troy", "Black")
print(user.first)
print(user2.first)