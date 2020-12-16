#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2:
            bool_list.append(False)
        else:
            bool_list.append(True)
    return bool_list


def main():
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_r = divisible_by_2(my_list)

    i = 0
    while i < len(list_r):
        if list_r[i]:
            print("{:d} {:s} divisible by 2".format(my_list[i], "is"))
        else:
            print("{:d} {:s} divisible by 2".format(my_list[i], "is not"))
        i += 1


if __name__ == "__main__":
    main()
