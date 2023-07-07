# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# # string = "a a a b c a a d c d d".split()
# # print(*string)
# # answer = ""
# new_list = []
# for elem in string:
#     if elem in new_list:
#         answer += elem + "_" + str(new_list.count(elem)) + " "
#     else:
#         answer += elem + " "
#     new_list.append(elem)
# # my_dict = {}
# # for elem in string:
# #     if elem in my_dict:
# #         answer += elem + "_" + str(my_dict[elem]) + " "
# #         my_dict[elem] +=1
# #     else:
# #         answer += elem + " "
# #         my_dict[elem] = 1
# # print(answer)


# my_list = set[1, 5, 5, 4, 7, 3, 3, 44]
# my_set = set(my_list)
# print(len(my_set))
# print(my_set)
# my_set.add(66)
# # my_set.remove(3)
# print(my_set)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


st = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure . So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
words = st.split()
print(len(set(words)))
my_dict = {}
for word in words:
    if word in my_dict:
        my_dict[word] +=1
    else:
        my_dict[word] = 1
print(my_dict)
values = my_dict.values()
max_value = max(values)
for key, value in my_dict.items():
    if value == max_value:
        print(key, value)