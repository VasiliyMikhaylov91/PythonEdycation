import csv


def load_db(path: str) -> list:
    if path.endswith('.csv'):
        with open(path, 'r', encoding='utf8') as file:
            return [ (';'.join(i)) for i in csv.reader(file)]
    else:
        with open(path, 'r', encoding='utf8') as file:
            return [i[:-1] if i.endswith('\n') else i for i in file]

def save_db(save_list: list, path: str):
    if path.endswith('.csv'):
        with open(path, 'w', encoding='utf8', newline='') as file:
            for row in save_list:
                csv.writer(file).writerow(row.split(';'))
    else:
        with open(path, 'w', encoding='utf8') as file:
            file.write('\n'.join(save_list))