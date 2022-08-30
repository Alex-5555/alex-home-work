'''
size = 5

     *
    ***
   *****  
  *******
 *********
     |
 _________    

'''
size = 5
for size_st in range(1, size+8):
    if size_st == 5:
        print('     '+'*')
    if size_st == 7:
        print('    '+'***')   
    if size_st == 8:
        print('   '+'*****')   
    if size_st == 9:
        print('  '+'*******')
    if size_st == 10:
        print(' '+'*********')   
    if size_st == 11:
        print('     '+'|')    
    if size_st == 12:
        print(' '+'_________')    
        
size = 15
for size_st in range(1, size+1):
    bc = size-size_st
    print(' '*bc +'*'*(size_st + (size_st-1)))

'''
    1 + 0 
    2 + 1
    3 + 2
    4 + 3
    5 + 4

'''
