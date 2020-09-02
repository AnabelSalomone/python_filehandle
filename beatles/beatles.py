import json
import sqlite3

conn = sqlite3.connect("beatles.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Album;

--sql
CREATE TABLE Album (
  id INTEGER NOT NULL PRIMARY KEY
  name TEXT UNIQUE
  cover TEXT 

)

''')

with open('tracks.json') as fhandle:
  dictionary = json.load(fhandle) #Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object


  cur.executescript
  for item in dictionary:
    print(item["name"])
