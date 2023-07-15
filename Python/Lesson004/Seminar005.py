# lst = []
# for i in range(1,10):
#     lst.append(i)
# print(lst)

# lst = [i for i in range(1,10)]
# print(lst)

# lst = [i**2 for i in range(1,10)]
# print(lst)

# string = input()
# lst = [int(i) for i in string.split()]
# print(lst)

# a = [1, 33, 44, 33]
# b = [i*2 for i in a]
# print(b)

# a = [1, 33, 4, 33, 6]
# b = [i*2 for i in a if i%2 ==0]
# print(b)

# def kvadrat(a):
#     return a*a

# n = int(input())
# print(kvadrat(n))

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# a = [1, 1, 1, 1, 1]
# min_elem = 1
# new_a = []
# for a_elem in a:
#     if a_elem <= 3:
#         new_a.append(a_elem)
#     else:
#         new_a.append(min_elem)
# print(new_a)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5


# def i_simple(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# print(i_simple(10))  



