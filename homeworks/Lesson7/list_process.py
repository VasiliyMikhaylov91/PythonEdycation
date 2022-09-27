def search(input_list: list, serch_str: str) -> list:
    return [i for i in input_list if serch_str in i]

def new_record(input_list: list, added_str: str) -> list:
    input_list.append(added_str)
    return input_list

def del_record(input_list: list, del_str: str) -> str:
    return [i for i in input_list if not (del_str in i)]