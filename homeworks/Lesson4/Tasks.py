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
# from random import randint
# def polynom(degree: int) -> str:
#     coeff = randint(0, 100)
#     if degree < 0:
#         return '=0'
#     if coeff != 0:
#         if degree == 0:
#             return  f'+{coeff}' + polynom(degree - 1)
#         elif degree == 1:
#             return f'+{coeff}*x' + polynom(degree - 1)
#         else:
#             return f'+{coeff}*x**{degree}' + polynom(degree - 1)
# result = polynom(int(input('Введите степень числа ')))[1:]
# print(result)
# with open('polynom.json', 'w') as polynom_file:
#     polynom_file.write(result)
'''
5 Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов
'''


# def polynom_reconstruction_list(polinom: str) -> list:
#     count = 1
#     while count != len(polinom):
#         if polinom[count] == '-':
#             polinom = polinom[:count] + '+' + polinom[count:]
#             count += 1
#         count += 1
#     polynom_list = polinom.split('+')
#     for i in range(len(polynom_list)):
#          if not('x' in polynom_list[i]):
#              polynom_list[i] += '*x**0'
#          if not('**' in polynom_list[i]):
#              polynom_list[i] += '**1'
#     polynom_list_of_list = []
#     for i in polynom_list:
#         polynom_list_of_list.append(list(map(int, i.split('*x**'))))
#     count = 0
#     while count != len(polynom_list_of_list):
#         if polynom_list_of_list[-1 - count][1] != count:
#             polynom_list_of_list.extend([0])
#             polynom_list_of_list.insert(- 1 - count, [0, count])
#             polynom_list_of_list.pop()
#             count -=1
#         count += 1
#     return polynom_list_of_list

# def list_reconstruction_polynom(polynomlist: list) -> str:
#     polynom = ''
#     for i in polynomlist:
#         if i[0] != 0:
#             if(0 != i[1] != 1):
#                 if i[0] < 0:
#                     polynom += f'{i[0]}*x**{i[1]}'
#                 else:
#                     polynom += f'+{i[0]}*x**{i[1]}'
#             elif (i[1] == 1):
#                 if i[0] < 0:
#                     polynom += f'{i[0]}*x'
#                 else:
#                     polynom += f'+{i[0]}*x'
#             else:
#                 if i[0] < 0:
#                     polynom += f'{i[0]}'
#                 else:
#                     polynom += f'+{i[0]}'
#     return polynom

# def polynom_list_summ(first_polynom: list, second_polynom: list) -> list:
#     if first_polynom[0][1] > second_polynom[0][1]:
#         max_digree_polynom = first_polynom
#         min_digree_polynom = second_polynom
#     else:
#         max_digree_polynom = second_polynom
#         min_digree_polynom = first_polynom
#     result_polynom = max_digree_polynom
#     for i in result_polynom:
#         for j in min_digree_polynom:
#             if i[1] == j[1]:
#                 i[0] += j[0]
#     return result_polynom

# with open('polynom_1.json', 'r') as polynom_file:
#     polynom_first = polynom_file.read()
# # Пример из файла:-32*x**4-41*x**3-21*x**2+42

# with open('polynom_2.json', 'r') as polynom_file:
#     polynom_second = polynom_file.read()
# # Пример из файла:21*x**2-4

# polynom_summ = list_reconstruction_polynom(polynom_list_summ\
#             (polynom_reconstruction_list(polynom_first),polynom_reconstruction_list(polynom_second)))

# with open('polynom_result.json', 'w') as polynom_file:
#     polynom_file.write(polynom_summ)
