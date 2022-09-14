'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
'''

# number = input('Введите вещественное число ')
# summ = 0
# for i in number:
#     if i != '.':
#         summ += int(i)

# print(f'Сумма цифр в числе {summ}')

'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
# list = []
# for i in range(1, int(input('Введите натуральное число ')) + 1):
#     if i == 1:
#         list.append(i)
#     else:
#         list.append(list[i - 2] * i)
# print(list)

'''
3 Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''

def sum_sequence(number: int) -> float:
    if number == 1:
        return 2
    return (1 + (1 / number)) ** number + sum_sequence(number - 1)

print(sum_sequence(int(input('Введите натуральное число '))))


# number = int(input('Введите натуральное число '))
# print ('{', end = '')
# for i in range(1, number + 1):
#     if i != number:
#         print(f'{i}: {round(((1 + 1/i) ** i), 2)},', end = ' ')
#     else:
#         print(f'{i}: {round(((1 + 1/i) ** i), 2)}' + '}')

'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
'''
# from random import randint

# element_numbers = int(input('Введите натуральное число '))
# list = []
# for i in range(element_numbers):
#     list.append(randint(-element_numbers, element_numbers))
# print(list)
# f = open('file.txt', 'w', encoding='utf-8')
# for i in range(1, randint(1, element_numbers)):
#     f.write(str(randint(0, element_numbers - 1)) + '\n')
# f.close()

# f = open('file.txt', 'r', encoding='utf-8')
# miltiplication = 1
# for line in f:
#     miltiplication *= int(line)
# f.close()
# print(miltiplication)
'''
5. Реализуйте алгоритм перемешивания списка.
'''
# from random import randint

# list = []
# for i in range(0, randint(1, 10)):
#     list.append(randint(0, 50))
# print(list)

# for i in range(1, randint(10, 20)):
#     first_sort_element = randint(0, len(list) - 1)
#     second_sort_element = randint(0, len(list) - 1)
#     temp = list[first_sort_element]
#     list[first_sort_element] = list[second_sort_element]
#     list[second_sort_element] = temp
# print(list)