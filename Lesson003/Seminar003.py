# Задача №17. Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]

# for elem in my_list:
#     i = 0
#     count = 0
#     if elem[i] == elem[i+1]:
#         i = i + 1
#     else:
#         count = count + 1
# print(count)

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# my_list_2 = []
# i = 0
# for elem in my_list:
#     if elem not in my_list_2:
#         my_list_2.append(elem) 
# print(len(my_list_2))

# Задача №19. Дана последовательность из N целых чисел и 
# число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

# my_list = [1, 2, 3, 4, 5]
# k = int(input('Введите число'))
# my_list_2 = my_list[k:] + my_list[:k]
# print(my_list, my_list_2)

# list1 = [1, 2, 3, 4, 5] 
# k = 2
# print(list1)

# for i in range(k):
#     last_elem = list1.pop()
#     list1.insert(0, last_elem)

# print(list1)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

# list1 = [0, -1, 5, 2, 2]
# count = 0

# for i in range(1, len(list1)):
#     if list1[i] > list1[i-1]:
#         count += 1

# print(count)