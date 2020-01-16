import sys
import requests

print(sys.version)
print(sys.executable) #where located on my computer

res = requests.get("https://news.ycombinator.com/")
print("Hello")
print(res)