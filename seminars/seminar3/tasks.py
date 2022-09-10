# Диджитализирую Python
'''
1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
'''
# import time

# def my_random(minn, maxx):
#     time.sleep(0.3)
#     return int((time.time() % 1  * (maxx - minn)) + minn)
# #                     0.9                  7           1

# for i in range(10):
#     print(my_random(1, 9))

import time

def random():
    interval = int(input('Введите желаемый интервал рандома: '))
    ms = time.time()*1000.0
    b = int(ms)
    d = ms - b
    answer = d * interval
    print(int(round(answer, 0)))
    return answer

random()

'''
2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
['efg23', '79234gefg', 'sdgs', 'g53']
'2'
['efg23', '79234gefg']
'''
# def serch_number(input_list, searching_number):
#     result_list = []
#     for i in list:
#         if number in i:
#             result_list.append(i)
#     return result_list

# list = ['345det', 'dst57', 'htd56878', '3cxe4564']
# number = '45'
# print(serch_number(list, list))


'''
3. Напишите программу, которая определит позицию второго вхождения 
строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
'''
# def second_entries(list_area, searching_string):
#     count_entries = 0
#     for i in range(0, len(list_area)):
#         if searching_string == list_area[i]:
#             count_entries +=1
#         if count_entries == 2:
#             return i
#     return -1


# print(second_entries(["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"))