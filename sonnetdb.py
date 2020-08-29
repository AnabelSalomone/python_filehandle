import sqlite3

conn = sqlite3.connect('sonnets.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE Sonnets (verse TEXT, count INTEGER)')

file_exists = False
file_ext = ".txt"

while not file_exists:
  fname_input = input('Enter Poem Name: ')
  fname = fname_input.replace(" ", "") + file_ext
  try:
    with open(fname) as fhandle:
      for line in fhandle:
        if not line.startswith('Love'): continue
        count += 1
        verse = line.rstrip()
        cur.execute('INSERT INTO Sonnets (verse, count) VALUES (?, ?)', (line, count,))
        conn.commit()

        sqlval = 'SELECT verse, count FROM Sonnets ORDER BY count'

        for i, row in cur.execute(sqlval):
          print(str(row[i]))
    file_exists = True
  except Exception:
    print("File not found")
    file_exists = False

