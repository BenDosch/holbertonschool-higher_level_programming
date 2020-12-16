#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [x for x in my_list]
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list


"""def replace_in_list(my_list, idx, element):
    other_list = [x for x in my_list]
    if idx >= len(my_list) and idx < 0:
        return other_list
    other_list[idx] = element
    return other_list


def main():
    test_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(test_list, idx, new_element)
    print(new_list)
    print(test_list)


if __name__ == "__main__":
    main()
"""
