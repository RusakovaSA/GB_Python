# Задача №1. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = 700
# m = 750
# days = m/n
# import math
# print(f"Машине потребуется {math.ceil(days)} дня, чтобы проехать {m} килиметров.")

# Задача №3. В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input("Введите количетсво учеников в первом классе: "))
# b = int(input("Введите количетсво учеников во втором классе: "))
# c = int(input("Введите количетсво учеников в третьем классе: "))
# import math
# desks = math.ceil((a + b + c)/2)
# print(f"Школе потребуется приобрести {desks} парты для формирования трех новых математических классов.")

# Задача №5. Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input("Введите номер вагона с головы состава: "))
# j = int(input("Введите номер вагона с хвоста состава: "))
# print(f"В электричке {j + i - 1} вагонов.")

# Задача №7. Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# i = int(input("Введите год: "))
# if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
#     print("Введенный вами год является високосным.")
# elif i % 100 == 0:
#     print("Введенный вами год не является високосным")
# else:
#     print("Введенный вами год не является високосным.")

