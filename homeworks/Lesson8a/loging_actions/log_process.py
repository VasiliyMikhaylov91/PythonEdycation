def add_to_log(note:str):
    with open('.\homeworks\Lesson8a\loging_actions\log.txt', 'a', encoding='utf8') as log:
        log.write(note+'\n')