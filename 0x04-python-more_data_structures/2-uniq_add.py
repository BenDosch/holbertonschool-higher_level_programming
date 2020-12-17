#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list[:])
    total = 0
    for x in my_set:
        total += x
    return total


def main():
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))


if __name__ == "__main__":
    main()
