from tkinter import *
from tkinter import filedialog as fd



def ret_opt(args):
        global option
        option = args
        phone_list.destroy()

def result_search():
    buttons = Frame()
    buttons.grid(row=1, column=1)
    button = Button(master=buttons ,text = 'OK', command= lambda: ret_opt('0'))
    button.pack()
 
def option_button():
    buttons = Frame()
    buttons.grid(row=1, column=0)
    button_search = Button(master=buttons, text='Поиск', command= lambda: ret_opt('1'))
    button_search.pack(side=LEFT)
    button_add = Button(master=buttons, text='Добавить', command= lambda: ret_opt('2'))
    button_add.pack(side=LEFT)
    button_del = Button(master=buttons, text='Удалить', command= lambda: ret_opt('3'))
    button_del.pack(side=LEFT)
    button_exit = Button(master=buttons, text='Выход', command= lambda: ret_opt('4'))
    button_exit.pack(side=LEFT)

def del_contact(length:int):
    buttons = Frame()
    buttons.grid(row=0,column=1)
    label = Label(master=buttons, text = '*')
    label.grid(row=0, column=0)
    for i in range(length):
        button = Button(master= buttons, height=1, text='Удалить', command= lambda:ret_opt(i))
        button.grid(column=0, row=i+1, pady = 1)
    

def show_list(input_list: list, window_title:str, funct):
    global phone_list
    phone_list = Tk()
    phone_list.title(window_title)
    subscribers = Frame()
    subscribers.grid(row=0, column=0, padx=5, pady=5)
    details_list = [i.split(';') for i in input_list]
    column_names = ['Фамилия','Имя','Телефон']
    for i in range(len(column_names)):
        label = Label(master = subscribers,text= column_names[i], foreground='Gold', width=20)
        label.grid(row=0, column=i+1)
    for i in range(len(details_list)):
        for j in range(len(details_list[i])):
            label = Label(master = subscribers, text=details_list[i][j], width=20)
            label.grid(row=i+1, column=j+1, pady=4)
    funct()
    phone_list.mainloop()
    return option

def request() -> str:
    def search_name():
        global name_search
        name_search = search_entry.get()
        search_window.destroy()
    search_window = Tk()
    search_window.title('Введите фамилию')
    search_window.geometry('300x50')
    search_entry = Entry(width= 20)
    search_entry.pack(side= LEFT)
    button = Button(master= search_window, text='Искать', command= lambda:search_name())
    button.pack(side= LEFT)
    search_window.mainloop()
    return name_search

def new_person() -> str:
    def create():
        global lname, fname, tel
        lname = entry_lname.get()
        fname = entry_fname.get()
        tel = entry_tel.get()
        new_window.destroy()
    new_window = Tk()
    new_window.title('Новый контакт')
    person = ['Фамилия', 'Имя', 'Телефон']
    for i in range(3):
        label = Label(text=person[i])
        label.grid(row=i, column=0)
    entry_lname = Entry(width=20)
    entry_lname.grid(row=0, column=1)
    entry_fname = Entry(width=20)
    entry_fname.grid(row=1, column=1)
    entry_tel = Entry(width=20)
    entry_tel.grid(row=2, column=1)
    button = Button(text='Создать контакт', command=create)
    button.grid(row=3, column=1)
    new_window.mainloop()
    return lname + ';' + fname + ';' + tel

def get_path() -> str:
    return fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                    ("CSV files", "*.csv"),
                   ("JSON files", "*.json")))
   