# Задача 26: Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation (x, y):
    if y == 0:
        return 1
    return x * exponentiation(x, y-1)

a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
print(f'Число {a} в степени {b} равно {exponentiation(a,b)}.')

