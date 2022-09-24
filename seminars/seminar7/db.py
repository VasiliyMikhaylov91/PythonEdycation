
def export(data: str):
    with open('data_base', 'a') as file:
        file.write(data + '\n')