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
def funct(esp_str:str) ->int:
    if not((plus:='+' in esp_str) or (minus:='-' in esp_str) or (mult:='*' in esp_str) or ('/' in esp_str)):
        return int(esp_str)
    if plus or minus:
        if plus and minus:
            if esp_str.find('+') < esp_str.find('-'):
                return funct(esp_str[:esp_str.find('+')]) + funct(esp_str[esp_str.find('+') + 1:])
            else:
                return funct(esp_str[:esp_str.find('-')]) - funct(esp_str[esp_str.find('-') + 1:])
        if plus:
            return funct(esp_str[:esp_str.find('+')]) + funct(esp_str[esp_str.find('+') + 1:])
        return funct(esp_str[:esp_str.find('-')]) - funct(esp_str[esp_str.find('-') + 1:])
    if mult:
        return funct(esp_str[:esp_str.find('*')]) * funct(esp_str[esp_str.find('*') + 1:])
    return funct(esp_str[:esp_str.find('/')]) / funct(esp_str[esp_str.find('/') + 1:])
    

exp = '1-2*3'
print(funct(exp))


'''
2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''

# arr = [1, 2, 3, 5, 1, 5, 3, 10]

# print([item for item in arr if arr.count(item) == 1])

# print(tuple(filter(lambda x: arr.count(x) == 1, arr)))