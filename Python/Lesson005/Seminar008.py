# f = open ('my_file.txt', 'r')
# f.read()
# f.close()

# with open('file.txt', 'r') as f:
    # st = f.read() первый способ считать строку

    # st = f.readline()  второй способ считать строку
    # st2 = f.readline()

    # st = f.readlines() в список строк считать

# print(st)   
# print(st2)

    # for string in f:  считается как строка
    #     print(string)

    # for string in f: считается как числа
    #     a = int(string)  
    #     print(a)
    
#     lst = [int(i) for i in f]  считается как числа в список
# print(lst)

#     lst = [i.strip() for i in f]  считается без служебных символов как строка
# print(lst)

# ////////////////////////////////////////////////////////////////////

# arr = ['1', '55', '33', '4', '2']
# arr = ['1\n', '55\n', '33\n', '4\n', '2']
# arr = [1, 44, 33, 2, 66]
# arr = list(map(lambda x: str(x)+'\n', arr))
# with open('file.txt', 'w') as f:
#     f.writelines(arr)

import os
# print(os.getcwd()) позволит узнать в какой папке я нахожусь
# os.chdir('new_dir') позволит открыть нужную директорию

