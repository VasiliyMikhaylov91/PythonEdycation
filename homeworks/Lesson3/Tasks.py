'''
1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
# from random import randint

# list = []
# for i in range (0, randint(1, 10)):
#     list.append(randint(0, 50))
# print(list)

# summ = 0
# for i in range(1, len(list), 2):
#     summ += list[i]
# print(f'Сумма элементов на нечетных позициях {summ}')

'''
2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
# from random import randint

# start_list = []
# for i in range (0, randint(1, 10)):
#     start_list.append(randint(0, 50))
# print(start_list, end=' => ')

# end_list = []
# for i in range(0, int(len(start_list)/2)):
#     end_list.append(start_list[i] * start_list[len(start_list) - 1 -i])
# print(end_list)

'''
3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
# from random import randint
# from math import floor

# list = []
# for i in range(0, randint(1, 10)):
#     list.append(randint(0, 15) + randint(0,100)/100)
# print(list)

# min_fraction = list[0] - floor(list[0])
# max_fraction = list[0] - floor(list[0])
# for i in range(0, len(list) - 1):  
#     if list[i] - floor(list[i]) < min_fraction:
#         min_fraction = list[i] - floor(list[i])
#     if list[i] - floor(list[i]) > max_fraction:
#         max_fraction = list[i] - floor(list[i])
# print(f'Разница между максимальным и минимальным значением дробной части элементов {round(max_fraction - min_fraction, 2)}')

'''
4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

# dec_number = int(input('Введите целое число '))
# bin_number = ''
# print(dec_number, end=' -> ')
# while dec_number > 0:
#     bin_number = str(dec_number % 2) + bin_number
#     dec_number = int(dec_number/2)
# print(bin_number)

'''
5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

list = [0]
fibonacci_number = int(input('Введите количество чисел ряда Фибоначчи '))
for i in range(1, fibonacci_number + 1):
    if (i == 1) or (i == 2):
        list.append(1)
    else:
        list.append(list[i - 1] + list[i - 2])
for i in range(0, fibonacci_number):
    if fibonacci_number%2 == 0:
        list.insert(i, list[- i - 1] * ((-1) ** (i + 1)))
    else:
        list.insert(i, list[- i - 1] * ((-1) ** i))
print(list)