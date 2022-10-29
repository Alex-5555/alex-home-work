# from ctypes import pointer


ranks = ['6','7','8','9','10','J','Q','K','A']
points = [6,7,8,9,10,11,12,13,14]
ranks.extend(points)
print(ranks)


ranks.insert(2,[9,9,999,9,9,9])
print(ranks)
print(ranks[2][2])



# ranks.remove('5')
# print(ranks)

# c = ranks.pop(10)
# print(c)

# ranks.index(9, [7 [,12]])
# print(ranks)

# c = ranks.count(10)
# print(c)



# c = [*ranks, *points]
# points_a = [str(x) for x in points]
# points_a = list(map(str, points)) 
# points_a = [x**2 for x in points if x%2 == 0]
# points_a = []
# for x in points:
#     if x%2 == 0:
#         points_a.append(x**2)
#     else:
#        points_a.append(x**3) 
# print(points_a)
# print(','.join(ranks),','.join(points_a))
# result = list(set(ranks) & set(points))
# print(result)
#for card in g:
#    print(card["points"])
# print(*points)
# for index, a in enumerate(points):
#     if 2<index<6:
#         points[index] = 1
# print(points)
# удаліть с 3 по 5
#  собрать вместе points и  ranks
# for index, a in enumerate(points):
#     if 2<index<6:
#         points.pop(index)
# print(points)