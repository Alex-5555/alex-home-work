a = ["a","b","c","d","e","f","j","h"]
b = ["1","2","3","4","5","6","7","8"]
a.reverse()
#print(a)
for index, line in enumerate(a):
    print(' ')
    if index%2 == 0:
        line_odd = True
    else:
        line_odd = False
    for index_cell, st in enumerate(b):
        if index_cell%2 == 0:
            cell_odd = True
        else:
            cell_odd = False
        color = 'null'
        if line_odd and cell_odd:
            color = 'black'
        if line_odd and not cell_odd:
            color = 'white'
        if not line_odd and cell_odd: 
            color = 'white'
        if not line_odd and not cell_odd: 
            color = 'black'
        print(line + st + '-'+color+' ', end='')
