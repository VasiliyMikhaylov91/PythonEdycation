'''
1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
# print (' '.join(filter(lambda x: not 'абв' in x,input('Введите текст ').split())))


'''
2 Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
'''
# from os import system
# from random import randint
# def start_menu():
#     system('cls')
#     print('Добро пожаловать в игру Greedy Sweets')
#     print('0 - Правила игры')
#     print('1 - Игрок против игрока')
#     print('2 - Игрок против бота')
#     print('3 - Игрок против умного бота')
#     print('4 - Выход из игры')
#     match menu_point:= input('Выберите пункт меню '):
#         case '0':
#             game_rules()
#         case '1':
#             game('players', randint(0,1))
#         case '2':
#             game('bot', randint(0,1))
#         case '3':
#             game('smart_bot', randint(0,1))
#         case '4':
#             print('Заходите ещё! Всегда будем рады сыграть!')
#     if menu_point != '4':
#         start_menu() 

# def game_rules():
#     system('cls')
#     print('На столе лежит 2021 конфета.')
#     print('Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.')
#     print('За один ход можно забрать не более чем 28 конфет.') 
#     print('Побеждает ток кто сделает последний ход.')
#     input('Для выхода в главное меню введите что-нибудь ')

# def bot_move(sweets_quantity: int, max_sweets: int) -> int:
#     if sweets_quantity <= max_sweets:
#         return sweets_quantity
#     else:
#         return randint(1, max_sweets)

# def smart_bot_move(sweets_quantity: int, max_sweets: int) -> int:
#     if (sm := sweets_quantity % (max_sweets + 1)) !=0:
#         return sm
#     else: 
#         return bot_move(sweets_quantity, max_sweets)

# def player_get_sweets(sweets_quantity: int, player_number:bool, max_sweets: int) -> int:
#     max_sweets = max_sweets if sweets_quantity > max_sweets else sweets_quantity
#     player = 'Игрок 2' if player_number else 'Игрок 1'
#     get_sweets = int(input(f'{player} Сколько хотите взять конфет? '))
#     while not (0 < get_sweets <= max_sweets):
#         get_sweets = int(input(f'{player} Вы ошиблись. Вы можете взять от 1 до {max_sweets} конфет. Сколько хотите взять?' ))
#     return get_sweets


# def game(game_mode: str, move: bool, sweets_on_table: int = 2021, sweets_limit = 28):
#     system('cls')
#     while sweets_on_table > 0:
#         print(f'Количество конфет на столе {sweets_on_table}')
#         move = not move
#         get_sweets = 0
#         sweets_limit = sweets_limit if sweets_on_table > sweets_limit else sweets_on_table
#         if move:
#             if game_mode == 'players':
#                 get_sweets = player_get_sweets(sweets_on_table, move, sweets_limit)
#             elif game_mode == 'bot':
#                 get_sweets = bot_move(sweets_on_table, sweets_limit)
#                 print(f'Бот взял {get_sweets}')
#             else:
#                 get_sweets = smart_bot_move(sweets_on_table, sweets_limit)
#                 print(f'Бот взял {get_sweets}')
#         else:
#             get_sweets = player_get_sweets(sweets_on_table, move, sweets_limit)
#         sweets_on_table -= get_sweets
#     if move:
#         if game_mode == 'players':
#             print('Игрок 2 победил!!! Поздравляем!')
#         else:
#             print('К сожалению бот победил :\ Cыграйте ещё')
#     else:
#         print('Игрок 1 победил!!! Поздравляем!')
#     input('Для выхода в главное меню введите что-нибудь ')

# start_menu()

'''
3 Создайте программу для игры в ""Крестики-нолики"".
'''
from os import system
def zero_chenge(x):
    return x if x != 0 else ' '

def show_field(field: list = []):
    system('cls')
    for i in range(0, 5):
        if i%2:
            print('-----------')
        else:
            row = int(i/2*3)
            print(f' {row + 1} | {row + 2} | {row + 3}')
    print()
    for i in range(0, 5):
        if i%2:
            print('-----------')
        else:
            row = int(i/2)
            print(f' {zero_chenge(field[row][0])} | {zero_chenge(field[row][1])} | {zero_chenge(field[row][2])}')

def coordinate(function, number:int)-> int:
    return function(number)

def check_identity(field: list, simbol:str) -> bool:
    for i in field:
        if fl_r := (i == [simbol, simbol, simbol]):
            return fl_r
    for i in range(len(field)):
        if fl_c := (field[0][i] == field[1][i] == field[2][i] != 0):
            return fl_c
    if (field[0][0] == field[1][1] == field[2][2] != 0) or\
        (field[-1][0] == field[-2][1] == field[-3][2] != 0):
        return True
    else:
        return False

def zero_absece(field: list) -> bool:
    for i in field:
        for j in i:
            if j == 0:
                return False
    else:
        return True

def game():
    game_list = []
    for i in range(0,3):
        game_list.append([0, 0, 0])
    show_field(game_list)
    move = False
    winer_flag = False
    full_field = False

    while not(winer_flag or full_field):
        move = not move
        word = "крестик" if move else "нолик"
        user_option = int(input(f'Куда поставить {word}? ')) - 1
        coordinate_line = coordinate(lambda x: x//3,user_option)
        coordinate_col = coordinate(lambda x: x%3 ,user_option)
        while not(0 <= user_option < 9) or (game_list[coordinate_line][coordinate_col] != 0):
            user_option = int(input(f'Туда нельзя поставить. Куда поставить {word}? ')) - 1
            coordinate_line = coordinate(lambda x: x//3,user_option)
            coordinate_col = coordinate(lambda x: x%3 ,user_option)
        sign = game_list[coordinate_line][coordinate_col] = 'X' if move else 'O'
        show_field(game_list)
        winer_flag = check_identity(game_list,sign)
        if winer_flag:
            print(f'{word}и победили! Ура, ура!')
        if (not winer_flag) and (full_field := zero_absece(game_list)):
            print('У нас ничья')

game()
            
'''
4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''