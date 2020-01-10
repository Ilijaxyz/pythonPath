''' Model playlist '''

song = {
  "title":"Hello",
  "artist": ["Doggo"],
  "date_added": '2019-12-04',
  "album_name":"One",
  "playlist":"Bus",
  "duration": 3
}

song2 = {
  "title":"Wof",
  "artist": ["Doggo"],
  "date_added": '2019-12-04',
  "album_name":"Two",
  "playlist":"Bus",
  "duration": 3
}

playlist = {
  "title":"Let's go",
  "songs": [song],
  "author": "Lele"
}

spotify = [playlist]

person = [["name", "Jared"],["job", "Musician"],["city", "Bern"]]

answer = { person[i][0]:person[i][1] for i in range(0,3) }
answer2 = dict.fromkeys("aeiou", 0)
answer3 = { i:chr(i) for i in range(65,90)}
# print(answer2)
# print(answer)

''' TUPLE IMMUTABLE  faster then LIST '''
x=(3,4,5,6)
''' SETS do not have duplicate and there is no order '''
s = { 1,2,3}

''' SET MATH 
Set intersection &
set union | '''

'''
Set comprenhension, list comprenhension and
dictionary comprenhension
'''
set1 = {x**2 for x in range(1,10)}
print(set1)
