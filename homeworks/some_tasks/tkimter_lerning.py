# import tkinter as tk

 
# window = tk.Tk()
# window.title('Введите домашний адрес')
 
# frame = tk.Frame(master=window, width=150, height=150, relief= tk.SUNKEN, borderwidth=3)
# frame.pack(fill=tk.X)
# frame.columnconfigure(1, minsize= 250)

# entry = [] 
# labels = []
# label_names = ['Имя', 'Фамилия:', 'Адрес 1:', 'Адрес 2:', 'Город:', 'Регион:', 'Почтовый индекс', 'Страна']
# for i in range(8):
#     labels.append(tk.Label(master=frame, text=label_names[i]))
#     labels[i].grid(row = i, column = 0, sticky = 'e')
#     entry.append(tk.Entry(master=frame))
#     entry[i].grid(row = i, column = 1, sticky = 'ew')

# frame_button = tk.Frame(master=window)
# frame_button.pack(fill=tk.X, ipadx=5, ipady=5)

# button_1 = tk.Button(master=frame_button,text='Отправить')
# button_1.pack(side = tk.RIGHT, padx=10, ipadx=10)

# button_2 = tk.Button(master=frame_button,text='Очистить')
# button_2.pack(side = tk.RIGHT, ipadx=10)
# window.mainloop()

from random import randint
import tkinter as tk

def Bones():
    lbl['text'] = str(randint(1,6))

window = tk.Tk()

button = tk.Button(master= window, text='Бросить', command=Bones)
button.pack()
lbl = tk.Label(text='')
lbl.pack()

window.mainloop()