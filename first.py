import sys
import requests

# print(sys.version)
# print(sys.executable) #where located on my computer

# res = requests.get("https://news.ycombinator.com/")
# print("Hello")
# print(res)
# print(res.headers)
# print(res.text) # made for browser

# url = "http://www.google.com"
# res = requests.get(url)
# print(f"{url} responded with status {res.status_code}")

''' 
Let's try to interact with an API
and get data in more understandable data
that we can pass to a dictionary or list
'''
# url = "https://icanhazdadjoke.com/"
# res = requests.get(url,headers = {"Accept": "application/json"  })
# data = res.json() # parse json to dictionary

# # print(f"Response  text: {res.text}")
# joke = data["joke"]
# print(f"Response  json: {joke}")

url = "https://icanhazdadjoke.com/search"
res = requests.get(
  url,
  headers = {"Accept": "application/json"  },
  params = {"term": "cat"}
)
data = res.json() # parse json to dictionary

# print(f"Response  text: {res.text}")

print(f"Response  json: {data['results']}")