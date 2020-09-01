import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect("tracks.sqlite")
cur = conn.cursor()

def lookup(d, key):
  found = False
  for child in d:
    if found : return child.text
    if child.tag == 'key' and child.text == key :
      found = True
  return None


stuff = ET.parse("./Library.xml")
all = stuff.findall('dict/dict/dict')

print('Dict count:', len(all))

for entry in all:
  if ( lookup(entry, 'Track ID') is None ) : continue

  name = lookup(entry, 'Name')
  artist = lookup(entry, 'Artist')
  album = lookup(entry, 'Album')
  length = lookup(entry, 'Total Time')

  if name is None or artist is None or album is None : 
      continue

  print(name, artist, album, length)