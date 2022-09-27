def load_db():
    with open('.\homeworks\Lesson7\data_phone.json', 'r', encoding='utf8') as file:
        return [i[:-1] if i.endswith('\n') else i for i in file]

def save_db(save_list):
    with open('.\homeworks\Lesson7\data_phone.json', 'w', encoding='utf8') as file:
        file.write('\n'.join(save_list))

