# a = [x for x in range(1,13) if x%2 == 0] 
# print(a)

date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
    **date_info,
    **track_info
 ) 
print(filename)   
