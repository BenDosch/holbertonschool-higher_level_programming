#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return(a_dictionary)


def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    [print("{}: {}".format(key, a_dictionary[key])) for key in keys]


def main():
    a_dict = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
    new_dict = simple_delete(a_dict, 'track')
    print_sorted_dictionary(a_dict)
    print("--")
    print_sorted_dictionary(new_dict)
    print("--")
    print("--")
    new_dict = simple_delete(a_dict, 'c_is_fun')
    print_sorted_dictionary(a_dict)
    print("--")
    print_sorted_dictionary(new_dict)


if __name__ == "__main__":
    main()
