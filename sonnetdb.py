import sqlite3

conn = sqlite3.connect('sonnets.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Sonnets')
cur.execute('CREATE TABLE Sonnets (verse TEXT, count INTEGER)')

file_ext = ".txt"
count = 0

fname_input = input('Enter Poem Name: ')
fname = fname_input.replace(" ", "") + file_ext
with open(fname) as fhandle:
  for line in fhandle:
    if not line.startswith('Love'): continue
    count = count + 1
    verse = line.rstrip()
    cur.execute('INSERT INTO Sonnets (verse, count) VALUES (?, ?)', (line, count,))
    conn.commit()

    sqlval = 'SELECT verse, count FROM Sonnets ORDER BY count'

    for row in cur.execute(sqlval):
      print(str(row))