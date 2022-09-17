'''
1. В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
1 2 3 5
'''
# def fun(inp_list):
#     for i in range(0, len(inp_list)):
#         if (inp_list[i] + 1) != inp_list[i + 1]:
#             return inp_list[i] + 1
# print(fun(list(map(int,input('Введите строку из чисел ').split()))))
our_string = list(map(int,'1 2 3 5'.split()))
print(list(item + 2 for item in range(len(our_string)-1) if our_string[item] + 1 != our_string[item + 1]))
'''
2. Дан список чисел. Создайте список, в который попадают числа, 
описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
    *Пример:* 
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
'''
# input_list = [1, 5, 2, 3, 4, 6, 1, 7]
# output_list = [input_list[0]]
# [output_list.append(item) for item in input_list if item > output_list[-1]]
# print(output_list)

'''
3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
'Мы неабв очень любим Питон иабв Джавуабв!'
'Мы очень любим Питон!'
'''
# print (' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))
