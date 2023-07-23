# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

def read_file():
    with open("phone_direct.txt", "r+", encoding="utf-8") as file:
        info = [i.strip() for i in file]
        return info

def write_file():
    pass

def print_info(info):
    print("№    **    ФИО    **    номер телефона")
    for id, info in enumerate(info):
        print(id + 1, info)

def search_info(info):
    # insert = input("Введите имя или фамилию: ")
    # info_1 = list(map(insert, info))
    # print(info_1)
    with open("phone_direct.txt", "r+", encoding="utf-8") as file:
        search = input("Введите имя или фамилию: ")
        # if info.count(search):
        #     print('Элемент присутствует в списке!')
        # else:
        #     print('Элемент отсутствует в списке!')
        # if len(search):
        #     print('Элемент присутствует в списке!')
        #     # print(*search)
        # else:
        #     print('Элемент отсутствует в списке!')
        res = list(filter(lambda x: search in x, info))
        print(str(res))

def change_info():
    pass

def delete_info(info):
    with open("phone_direct.txt", "r+", encoding="utf-8") as file:
        index_del = int(input("Введите номер строки на удаление: "))
        info.pop(index_del - 1)
        print(f"Строка {index_del} с записью удалена.")
        print("")
        print_info(info)

def menu():
    info = read_file()
    while True:
        print("Выберите действие: ")
        print("1 - вывести информацию на экран")
        print("2 - поиск данных")
        print("3 - изменение данных")
        print("4 - удаление данных")
        print("0 - выход из программы")
        n = int(input("Ваш выбор: "))
        print("")
        if n == 0:
            break
        elif n == 1:
            print_info(info)
            print("")
        elif n == 2:
            search_info(info)
            print("")
        elif n == 3:
            pass
        elif n == 4:
            delete_info(info)
            print("")


if __name__ == "__main__":
    menu()
