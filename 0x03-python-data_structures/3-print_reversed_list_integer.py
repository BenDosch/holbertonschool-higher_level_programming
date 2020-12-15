#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    for i in range(len(my_list)):
        my_list.reverse()
        print("{:d}".format(my_list[i]))
        my_list.reverse()


def main():
    test_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(test_list)


if __name__ == "__main__":
    main()
