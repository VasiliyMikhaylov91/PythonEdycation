'''
1 Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

# from math import pi

# def definition_convert(float_definition: float) -> int:
#     converse_float = int(1 / float_definition)
#     count = 0
#     while converse_float > 0:
#         converse_float = int(converse_float / 10)
#         count +=1
#     return count - 1

# print(round(pi, definition_convert(float(input('Введите точность числа пи в десятых долях ')))))

'''
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
# def simple_numbers(decomposition_number: int, div_number: int = 2, result_list: list = []) -> list:
#     if 0 <= decomposition_number <= div_number :
#         result_list.append(decomposition_number)
#         return result_list
#     if decomposition_number % div_number == 0:
#         result_list.append(div_number)
#         return simple_numbers(decomposition_number // div_number, div_number, result_list)
#     return simple_numbers(decomposition_number, div_number + 1, result_list)
# print(simple_numbers(int(input('Введите число '))))

'''
3 Задайте последовательность чисел.  Напишите программу, которая выведет 
список неповторяющихся элементов исходной последовательности.
'''

# def uniq_list(number_list: list) -> list:
#     new_list = []
#     for i in number_list:
#         if not (i in new_list):
#             new_list.append(i)
#     return new_list

# print(uniq_list([input('Введите число ') \
#     for i in range(int(input('Введите количество элементов списка ')))]))

'''
4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
from random import randint
def polynom(degree: int, result_str: str = '') -> str:
    coeff = randint(0, 100)
    if degree < 0: 
        return str
    if coeff == 0:
         return polynom(degree - 1, str)
    if degree == 0: 
        return polynom(degree - 1, str + f'+{coeff}')
    if degree == 1: 
        return polynom(degree - 1, str + f'+{coeff}*x')
    return polynom(degree - 1, str + f'+{coeff}*x^{degree}')
print(polynom(int(input('Введите степень числа '))))
'''
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов
'''
