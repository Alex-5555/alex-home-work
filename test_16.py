a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for my_file in a:
    f = open(my_file, 'w+')
    f.write('Alex ' + my_file)
    f.close()
  
