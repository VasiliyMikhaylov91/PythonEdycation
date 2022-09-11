'''
Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел. 
'''
# user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
# numbers = list(map(int, user_string))
# print(max(numbers), min(numbers))

'''
Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
1) с помощью математических формул нахождения корней квадратного уравнения 
2) с помощью дополнительных библиотек Python 
'''
# from math import *

# def square_root(a: int = 0, b: int = 0, c: int = 0) -> list:
#     discriminant = (b ** 2) - (4 * a * c)
#     if discriminant < 0:
#         return []
#     elif discriminant == 0:
#         x = - (b / (2 * a))
#         return [x]

#     x1 = (-b + sqrt(discriminant)) / (2 * a)
#     x2 = (-b - sqrt(discriminant)) / (2 * a)
#     return [x1, x2]
    
# print('Ax² + Bx + C = 0')
# a = int(input('A= '))
# b = int(input('B= '))
# c = int(input('C= '))
# print(square_root(a, b, c))
'''
Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
'''
def less_common_div(first_number: int, second_number: int) -> int:
    minimal_number = min[first_number, second_number]
    for i in range(2, minimal_number + 1):
        if (first_number % i == 0) and (i % second_number % i == 0):
            return i
    return None

print(less_common_div(int(input('Введите первое число ')), int(input('Введите второе число '))))
    