'''
1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
from random import randint
def summ_unhones(summ_list: list) -> int:
    summ = 0
    for i in range(1, len(summ_list), 2):
        summ += summ_list[i]
    return summ

input_list = []
for i in range (0, randint(1, 10)):
    input_list.append(randint(0, 50))

print(f'{input_list} -> {summ_unhones(input_list)}')

# summ = 0
# for i in range(1, len(list), 2):
#     summ += list[i]
# print(f'Сумма элементов на нечетных позициях {summ}')

'''
2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
# from random import randint
# from math import ceil

# start_list = []
# for i in range (0, randint(1, 10)):
#     start_list.append(randint(0, 50))
# print(start_list, end=' => ')

# end_list = []
# for i in range(0, ceil(len(start_list)/2)):
#     end_list.append(start_list[i] * start_list[- 1 - i])
# print(end_list)

'''
3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
# from random import randint
# from math import floor

# def differ_max_min_fraction(float_list: list) -> float:
#     min_fraction = float_list[0] - floor(float_list[0])
#     max_fraction = float_list[0] - floor(float_list[0])
#     for i in range(0, len(float_list)):
#         fraction = float_list[i] - floor(float_list[i])
#         if fraction < min_fraction:
#             min_fraction = fraction
#         if fraction > max_fraction:
#             max_fraction = fraction
#     return round((max_fraction - min_fraction),2)

# input_list = []
# for i in range(0, randint(1, 10)):
#     input_list.append(randint(0, 15) + randint(0,100)/100)

# print(f'{input_list} => {differ_max_min_fraction(input_list)}')
'''
4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
# def decimal_bin_converting(decimal_value: int, binary_value: str = '') -> str:
#     if decimal_value > 0:
#         return decimal_bin_converting(int(decimal_value/2), str(decimal_value % 2) + binary_value)
#     else:
#         return binary_value

# dec_number = int(input('Введите целое число '))
# print(f'{dec_number} -> {decimal_bin_converting(dec_number)}')

'''
5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

# def Fibonacci(number: int, first: int = 1, second: int = 1) -> int:
#     if number == 1 or number == 2:
#         return second
#     else:
#         return Fibonacci(number - 1, second, first + second)

# fibonacci_number = int(input('Введите количество членов ряда Фибоначчи '))
# list = [0]

# for i in range(1, fibonacci_number + 1):
#     list.append(Fibonacci(i))
#     list.insert(0, list[-1] * ((-1) ** (i + 1)))
# print(list)
