import os 
dirs = '111|222'
files = 'dima.txt,alex.txt'
content = 'zharikov;safonov'
content_a = [x for x in content.split(';')]
files_a = [x for x in files.split(',')]
dir = dirs.split('|')
for index, f in enumerate(files_a):
    os.mkdir(dir[index])
    my_file = open(dir[index] + '/' + f, 'w+')
    my_file.write(content_a[index])
    my_file.close()

# os.mkdir('alex')
# os.mkdir('dima')
# sps_dir = [, dir_2]
# for f in sps_dir
