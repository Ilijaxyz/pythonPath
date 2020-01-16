import requests
from random import randint
import pyfiglet
from colorama import init, deinit
from termcolor import colored
init()

header = pyfiglet.figlet_format("DAD JOKE 9000!")


print(colored(header, 'green'))
user_input = input("Let me tell a joke, give me a topic? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
  url,
  headers = {"Accept":"application/json"},
  params = {"term": user_input}
)
data = res.json() #turn joson to dictionary
jokes = data['results']

if len(jokes) == 0:
  print(f"Sorry I don't have any jokes about {user_input}. Please try again.")
elif len(jokes) == 1:
  print(f"Here is one joke:")
  print(f"\n{jokes[0]['joke']}")
else:
  print(f"I have {len(jokes)} jokes about {user_input}. Here it is:")
  print(f"\n{jokes[randint(0,len(jokes)-1)]['joke']}")

deinit()