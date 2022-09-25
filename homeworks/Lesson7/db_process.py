def load_db():
    with open('.\homeworks\Lesson7\data_phone.txt', 'r', encoding='utf8') as file:
        # result = []
        # for i in file:
        #     result.append(i[:-1])
        return [i[:-1] if i.endswith('\n') else i for i in file]

def save_db(save_list):
    with open('.\homeworks\Lesson7\data_phone.txt', 'w', encoding='utf8') as file:
        file.write('\n'.join(save_list))