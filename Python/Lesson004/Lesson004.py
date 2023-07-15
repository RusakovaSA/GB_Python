# def calc2(x, y):
#     return x * y

# def math(op, a, b):
#     print (op(a, b))

# math(lambda x,y: x + y, 5, 25)

# array = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in array:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)
# ///////////////////////////////////////////
# array = [1, 2, 3, 5, 8, 15, 23, 38]

# def where(f, col):
#     return [x for x in col if f(x)]


# res = map(int, array)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
# ||||||||||||||||||||||||||||||||||||||||||||||||

# list_1 = [x for x in range(1, 10)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)
# ///////////////////////////////////////////////

# data = '22 44 66 88 99'
# print(data)

# data = list(map(int, data.split()))
# print(data)
# ||||||||||||||||||||||||||||||||||||||||||||||

# data = [1, 2, 3, 5, 8, 15, 23, 38, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)
# ||||||||||||||||||||||||||||||||||||||||||||

# data = [1, 2, 3, 5, 8, 15, 23, 38, 175]
# res = map(int, data)
# print(res)
# res = filter(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
# |||||||||||||||||||||||||||||||||||||||||||

# colors = ['red', '9999999', 'green']
# data = open('file.txt', 'a')
# data. writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()    