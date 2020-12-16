#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    other_list = [x for x in my_list]
    if idx >= len(my_list) or idx < 0:
        return other_list
    else:
        other_list[idx] = element
        return other_list
