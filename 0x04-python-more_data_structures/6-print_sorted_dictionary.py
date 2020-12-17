#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    [print("{}: {}".format(key, a_dictionary[key])) for key in keys]


def main():
    a_dict = {'language': "C", 'Num': 89, 'track': "Low-lvl", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dict)

if __name__ == "__main__":
    main()
