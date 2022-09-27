import os
import db_process, gui, list_process


def phone_info_process():
    cont_process = True
    phone_list = db_process.load_db()
    while cont_process:
        os.system('cls')
        gui.show_list(phone_list)
        print()
        match gui.request('1 - Поиск по фамилии\n2 - Добавить в справочник\n3 - Удалить из справочника\n4 - Выход\nВыберите действие: '):
            case '1':
                os.system('cls')
                gui.show_list(list_process.search(phone_list, gui.request('Введите фамилию ')))
                input()
            case '2':
                os.system('cls')
                phone_list = list_process.new_record(phone_list, gui.new_person())
            case '3':
                phone_list = list_process.del_record(phone_list, gui.request('Кого удалить? '))
            case '4':
                db_process.save_db(phone_list)
                cont_process = False
