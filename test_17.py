files = 'dima.txt,alex.txt'
content = 'zharikov;safonov'
content_a = [x for x in content.split(';')]
files_a = [x for x in files.split(',')]
for index, f in enumerate(files_a):
    my_file = open(f, 'w+')
    my_file.write(content_a[index])
    my_file.close()

