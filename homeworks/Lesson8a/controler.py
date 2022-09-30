import os
import Data.db_process as dp, Interfase.gui as gi, functions.list_process as lp

def phone_info_process():
    cont_process = True
    phone_list = dp.load_db(file_path := gi.get_path())
    while cont_process:
        match gi.show_list(phone_list,'Список контактов', gi.option_button):
            case 'search':
                gi.show_list(lp.search(phone_list,gi.request()), 'Результаты поиска', gi.result_search)
            case 'add':
                lp.new_record(phone_list, gi.new_person())
            case 'delete':
                phone_list = lp.del_record(phone_list, gi.show_list(phone_list,'Кого удалить?', lambda: gi.del_contact(len(phone_list))))
            case 'exit':
                dp.save_db(phone_list, file_path)
                cont_process = False
