from tkinter import *  
  
  
def clicked(inter):  
    btn.configure(text=f"Я же просил...{inter}")  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
# lbl = Label(window, text="Привет", font=("Arial Bold", 50))  
# lbl.grid(column=0, row=0)  
a = 4
btn = Button(window, text="Не нажимать!",command= lambda: clicked(a))  
btn.grid(column=1, row=0, padx=5, pady=5)  
window.mainloop()