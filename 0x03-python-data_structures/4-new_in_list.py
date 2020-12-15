#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    copy_list = []
    if my_list:
        for i in range(len(my_list)):
            copy_list.append(my_list[i])
    if idx < len(my_list) and idx >= 0:
        copy_list[idx] = element
    return (copy_list)


def main():
    test_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(test_list, idx, new_element)
    print(new_list)
    print(test_list)


if __name__ == "__main__":
    main()
