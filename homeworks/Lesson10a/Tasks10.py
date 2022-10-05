'''
1. Даны два списка чисел. Найдите все числа, которые входят как в первый, 
так и во второй список и выведите их в порядке возрастания
'''
# List_1 = [5, 8, 10, 43, 84]
# List_2 = [1, 9, 5, 24, 36, 10, 84]

# print(sorted(list(set(List_1) & set(List_2))))

'''
2. Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности 
или NO, если не встречалось
'''

# inp_str = '1 3 2 1 8 3 6 6'.split()

# print(['YES' if (inp_str[i] in inp_str[:i]) else "NO" for i in range(len(inp_str))])

'''
Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
Sample Input:
4
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

Sample Output:
19
'''
inp_text = '''4
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.'''
print(len(list(set(inp_text.replace('\n', ' ').split()[1:]))))