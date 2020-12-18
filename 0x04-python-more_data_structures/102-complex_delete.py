#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_d = list(a_dictionary.items())
    for i in range(len(a_d)):
        if a_d[i][1] == value:
            a_dictionary.pop(a_d[i][0])
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    [print("{}: {}".format(key, a_dictionary[key])) for key in keys]


def main():
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)


if __name__ == "__main__":
    main()
