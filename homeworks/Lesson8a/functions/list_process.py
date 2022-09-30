def search(input_list: list, serch_str: str) -> list:
    return list(filter(lambda x: serch_str in x, input_list))

def new_record(input_list: list, added_str: str) -> list:
    input_list.append(added_str)
    return input_list

def del_record(input_list: list, del_number: int) -> list:
    input_list.pop(del_number)
    return input_list

def chenge_record(where_list: list, chenge_number: int, chenge_str: str) -> list:
    where_list[chenge_number] = chenge_str
    return where_list