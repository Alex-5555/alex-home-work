import os
#os.mkdir('test')
#print('Creating test folder (directory)')
dirs = '1|2|3'
for dir in dirs.split('|'):
    path_dir = 'test/'+dir
    os.mkdir(path_dir)
    print(path_dir)