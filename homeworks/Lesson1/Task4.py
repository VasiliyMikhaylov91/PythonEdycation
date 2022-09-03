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