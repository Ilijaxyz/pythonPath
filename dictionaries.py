''' Dictionaries  data structures

    describing data in more detail
  keys are almost always string and numbers
  values can 
'''

instructor = {
  "name" : "Bajo hahahhaha",
  "owns_dog": True,
  "num_courses": 4,
  "favourite_language": "Python",
  "is_hilarious": True,
  44: "his favourite number"
}

another_dictionary = dict( 
  name = "doggo",
  age = 8)

#access dictionary

# print(instructor["name"])
# print(another_dictionary)

for v in instructor.values():
  print(v)

for k in instructor.keys():
  print(k)

for k, v in instructor.items():
  print(f"{k} {v}")