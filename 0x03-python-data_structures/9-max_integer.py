#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if not my_list:
        return None
    else:
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max


def main():
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))


if __name__ == "__main__":
    main()
