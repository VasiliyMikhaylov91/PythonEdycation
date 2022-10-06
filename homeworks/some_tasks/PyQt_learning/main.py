from PyQt5 import QtCore, QtGui, QtWidgets as QW
import sys
# import design

# class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)

# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение

# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()

class Window(QW.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QW.QLabel(self)

        self.main_text = QW.QLabel(self)
        self.main_text.setText('Это базовая надпись')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QW.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText('Нажми на меня')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText('Вторая надпись')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QW.QApplication(sys.argv)
    window = Window()

    

    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    application()