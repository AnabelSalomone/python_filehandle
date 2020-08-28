fexists = False

while not fexists:
  file_name = input("Enter the file name: ")
  try:
    with open(file_name) as fhandle:
      for line in fhandle:
        stripped_line = line.rstrip()
        print(stripped_line)
    fexists = True
  except:
    fexists = False

chosen_word = input("\n Which word would you like to find?") 
with open(file_name) as fhandle:
  for line in fhandle:
    if chosen_word in line:
      print(line)
 