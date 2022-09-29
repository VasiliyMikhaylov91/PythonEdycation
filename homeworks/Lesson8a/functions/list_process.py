def search(input_list: list, serch_str: str) -> list:
    return list(filter(lambda x: serch_str in x, input_list))

def new_record(input_list: list, added_str: str) -> list:
    input_list.append(added_str)
    return input_list

def del_record(input_list: list, del_number: int) -> str:
    input_list.pop(del_number)
    return input_list