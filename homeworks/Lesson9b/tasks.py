'''
1.Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и 
возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
'''
# def to_dict(lst:list)->dict:
#     res_dict = {}
#     for i in lst:
#         res_dict.setdefault(i,i)
#     return res_dict

# print(to_dict(['adad', 1, (1,2)]))

'''
2. Иван решил создать самый большой словарь в мире. 
Для этого он придумал функцию biggest_dict(**kwargs), 
которая принимает неограниченное количество параметров 
«ключ: значение» и обновляет созданный им словарь my_dict, 
состоящий всего из одного элемента «first_one» со значением «we can do it». 
Воссоздайте эту функцию.
'''

# def biggest_dict(**kwaegs):
#     with open ('homeworks\Lesson9b\my_dict.txt', 'a', encoding = 'utf8') as f:
#         for i in kwaegs:
#             f.write(f'{i}:{kwaegs[i]}\n')
# biggest_dict(some_else_key='something_esle', another_else_key='anything_else')

'''    
3.Дана строка в виде случайной последовательности чисел от 0 до 9. 
Требуется создать словарь, который в качестве ключей будет принимать данные числа 
(т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. 
Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. 
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел. 
'''

# def count_it(sequence):
#     first_countig_number = second_countig_number = therd_countig_number = 0
#     first_count_el = second_count_el = therd_count_el = 0
#     list_element = []
#     for i in range(len(sequence)):
#         if not(sequence[i] in list_element):
#             list_element.append(sequence[i])
#             count_i = sequence.count(sequence[i])
#             if count_i > first_countig_number:
#                 therd_count_el = second_count_el
#                 second_count_el = first_count_el
#                 first_count_el = i
#                 therd_countig_number = second_countig_number
#                 second_countig_number = first_countig_number
#                 first_countig_number = count_i
#             elif count_i > second_countig_number:
#                 therd_count_el = second_count_el
#                 second_count_el = i
#                 therd_countig_number = second_countig_number
#                 second_countig_number = count_i
#             elif count_i > therd_countig_number:
#                 therd_count_el = i
#                 therd_countig_number = count_i
#     return {
#         int(sequence[first_count_el]):first_countig_number,
#         int(sequence[second_count_el]):second_countig_number,
#         int(sequence[therd_count_el]):therd_countig_number
#     }
# print(count_it('11122222884555'))

'''
4.* (вместо задачи 3) Написать функцию thesaurus_adv(), 
принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
в котором ключи — первые буквы фамилий, а значения — словари, 
реализованные по схеме предыдущего задания и содержащие записи, 
в которых фамилия начинается с соответствующей буквы. 
Например: 
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева") 
{ "А": { "П": ["Петр Алексеев"] }, "И": { "И": ["Илья Иванов"] }, 
"С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] } }
'''
def thesaurus_adv(*args):
    dictionary = {}
    for i in args:
        d_items = i.split()
        if not(d_items[1][0] in dictionary.keys()):
            dictionary.setdefault(d_items[1][0],{d_items[0][0]:[i]})
        else:
            if not(d_items[0][0] in dictionary[d_items[1][0]].keys()):
                dictionary[d_items[1][0]].setdefault(d_items[0][0],[i])
            else:
                dictionary[d_items[1][0]][d_items[0][0]].append(i)
    return sorted(dictionary.items())
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))