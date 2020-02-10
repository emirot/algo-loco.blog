
def find_missing_number(list_numbers):
    s_list_number = set(list_numbers)
    for i in range(1, 10):
        if i not in s_list_number:
            return i