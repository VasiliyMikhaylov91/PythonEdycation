from tkinter import filedialog as fd

def show_list(input_list: list):
    for i in input_list:
        print(i.replace(';',' '))

def request(text:str) -> str:
    return input(text)

def new_person() -> str:
    return input('Введите фамилию ') + ';' + input('Введите имя ') + ';' + input('Введите телефон ')

def get_path() -> str:
    return fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                    ("CSV files", "*.csv"),
                   ("JSON files", "*.json")))