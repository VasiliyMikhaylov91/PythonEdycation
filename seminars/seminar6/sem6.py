'''
1. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный. 
    *Пример:* 
    2+2 => 4; 
    1+2*3 => 7; 
    1-2*3 => -5;
    
    - Добавьте возможность использования скобок, меняющих приоритет операций.
        
        *Пример:* 
        
        1+2*3 => 7; 
        
        (1+2)*3 => 9;
'''
def funct(esp_str:str) -> int:
    par_open=esp_str.find('(')
    if par_open != -1:
        return funct(esp_str[:par_open] + str(funct(esp_str[par_open + 1:(par_close := esp_str.find(')'))])) \
            + (esp_str[par_close + 1:] if par_close != len(esp_str) else ''))
    plus=esp_str.find('+')
    minus=esp_str.find('-')
    mult=esp_str.find('*') 
    div = esp_str.find('/')
    if (plus == -1) and (minus == -1) and (mult == -1) and (div == -1):
        return int(esp_str)
    if plus != -1:
        return funct(esp_str[:plus]) + funct(esp_str[plus + 1:])
    if minus != -1:
        return funct(esp_str[:minus]) - funct(esp_str[minus + 1:])
    if mult != -1:
        return funct(esp_str[:mult]) * funct(esp_str[mult + 1:])
    return funct(esp_str[:div]) / funct(esp_str[div + 1:])
    

exp = '1+(2*3)/3'
print(funct(exp))


'''
2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''

# arr = [1, 2, 3, 5, 1, 5, 3, 10]

# print([item for item in arr if arr.count(item) == 1])

# print(tuple(filter(lambda x: arr.count(x) == 1, arr)))