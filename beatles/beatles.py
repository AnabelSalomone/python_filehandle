import json
import sqlite3

conn = sqlite3.connect("beatles.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Album;

CREATE TABLE Album (
  id INTEGER NOT NULL PRIMARY KEY,
  name TEXT UNIQUE,
  cover TEXT
); 
''')

with open('tracks.json') as fhandle:
  dictionary = json.load(fhandle) #Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object

  for item in dictionary:
    item_id = item["id"]
    name = item["name"]
    cover = item["cover"]
    cur.execute('INSERT INTO Album (id, name, cover) VALUES (?, ?, ?)', (item_id, name, cover,))
    conn.commit()
