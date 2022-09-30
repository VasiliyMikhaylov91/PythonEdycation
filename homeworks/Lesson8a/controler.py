import Data.db_process as dpr, Interfase.gui as gi, functions.list_process as lp
from loging_actions.log_process import add_to_log

def phone_info_process():
    
    phone_list = dpr.load_db(file_path:= gi.get_path())
    add_to_log(f'Open {file_path}')
    cont_process = True
    while cont_process:
        try:
            match op:=gi.show_list(phone_list,'Список контактов', gi.option_button):
                case 'search':
                    gi.show_list(lp.search(phone_list,wd:=gi.request()), 'Результаты поиска', gi.result_search)
                    add_to_log(f'{op}:{wd}')
                case 'add':
                    lp.new_record(phone_list, who:=gi.new_person())
                    add_to_log(f'{op}:{who}')
                case 'delete':
                    del_person = str(phone_list[(dp:=gi.show_list(phone_list,'Кого удалить?', lambda: gi.del_chenge_contact(len(phone_list))))])
                    phone_list = lp.del_record(phone_list, dp)
                    add_to_log(f'{op}:{del_person}')
                case 'change':
                    num = gi.show_list(phone_list,'Кого изменить?', lambda: gi.del_chenge_contact(len(phone_list)))
                    chenge_parson = str(chp:=phone_list[num])
                    phone_list = lp.chenge_record(phone_list, num, gi.new_person(chp))
                    add_to_log(f'{op}:{chenge_parson} -> {phone_list[num]}')
                case 'exit':
                    dpr.save_db(phone_list, file_path)
                    cont_process = False
                    add_to_log (f'{op}: save to {file_path}')
        except:
            continue