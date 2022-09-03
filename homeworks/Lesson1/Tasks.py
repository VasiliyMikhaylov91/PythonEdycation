'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''

if int(input('Введите номер дня недели ')) < 6:
    print("Этот день не выходной")
else:
    print("Этот день выходной")

'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print('X    Y    Z    Res')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'{x}    {y}    {z}    {not(x or y or z) == (not x and not y  and not z)}')

'''
Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

x = int(input('x = '))
y = int(input('y = '))
print('square = ', end = ' ')
if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
else:
    if y > 0:
        print('2')
    else:
        print('3')

'''
Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

square = input('square (1 ... 4) ')
if ('1' in square) or ('4' in square):
    x_range = 'x > 0'
else:
    x_range = 'x < 0'
if ('1' in square) or ('2' in square):
    y_range = 'y > 0'
else:
    y_range = 'y < 0'
print(f'{x_range}  {y_range}')

'''
Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

a = [int(input('Введите координату x точки A ')), int(input('Введите координату y точки A '))]
b = [int(input('Введите координату x точки B ')), int(input('Введите координату y точки B '))]
print(f'Расстояние между точками {round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5, 2)}')