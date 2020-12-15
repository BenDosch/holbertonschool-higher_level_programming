#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list) and idx >= 0:
        return (my_list[idx])
    return (None)


def main():
    test_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(test_list, idx)))


if __name__ == "__main__":
    main()
