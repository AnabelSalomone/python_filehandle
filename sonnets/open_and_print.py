fhandle = open('sonnet116.txt')
sonnet = fhandle.readlines()

for full_line in sonnet:
  line = full_line.rstrip() #removes newline character at the end
  if line.startswith('Love'):
    if not "alters" in line: 
      print(line) 