'''
keeps python files small

like functions for DRY

reuse code across multiple files by importing

modul is just a python file

IMPORT ONLY WHAT YOU NEED
from MODULE import <METHOD_NAME>
'''
from termcolor import colored, cprint
from pyfiglet import Figlet
from keyword import iskeyword
from modules_part import get_customers


def contains_keyword(strings):
    for s in strings:
        if iskeyword(s):
            return True
    return False
# print(contains_keyword(["test", "test5","test5","return"]))

# print(get_customers())


'''
EXTERNAL MODULES
(online on a server)
'''


# from termcolor import colored
# text = colored("HELLOOO WORLD", color="magenta")
# print(text)

'''ASCII ART '''
message = input("What message you wanna print? ")
color_input = input("What color? ")

f = Figlet(font="slant")
formated = f.renderText(message)

cprint(formated, 'green', 'on_red')  # does not work on windows terminal
# print(colored)
# help(Figlet)


'''
autopep8 --in-place <filename>
'''
