#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            quotent = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            quotent = 0
        except ZeroDivisionError:
            print("division by 0")
            quotent = 0
        except IndexError:
            print("out of range")
            quotent = 0
        new_list.append(quotent)
    return new_list
