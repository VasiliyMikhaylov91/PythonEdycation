'''
1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0.56 -> 11
'''

# print(sum(map(int, [item for item in input('Введите вещественное число ') if item != '.'])))

'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
# def fun(x):
#     return 1 if x == 1 else x * fun(x - 1)
# print(list(fun(i) for i in range(1, int(input('Введите натуральное число ')) + 1)))

'''
3. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
# print(tuple(((not(x and y and z) == (not(x) or not(y) or not(z))) for z in range(2) for y in range(2) for x in range(2))))

'''
4. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5.0, 10.01] => 0.19
'''

input = [1.1, 1.2, 3.1, 10.01]
print(max(map(fract := lambda x: float(fr:=str(x).split('.')[1])/10**(len(fr)), input)) - min(map(fract, input)))

'''
5. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
# from math import ceil
# input = [2, 3, 4, 5, 6]
# print(list(input[i] * input[-i-1] for i in range(ceil(len(input)/2))))