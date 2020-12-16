#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            new_string += my_string[i]
    return new_string


def main():
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))


if __name__ == "__main__":
    main()
