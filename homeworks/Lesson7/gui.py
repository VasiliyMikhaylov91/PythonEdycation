import tkinter as tk

def show_list(input_list: list):
    for i in input_list:
        print(i)

def request(text:str) -> str:
    return input(text)

def new_person() -> str:
    return input('Введите фамилию ') + ' ' + input('Введите имя ') + ' ' + input('Введите телефон ')