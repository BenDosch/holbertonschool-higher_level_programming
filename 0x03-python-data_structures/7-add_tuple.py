#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a0 = 0
        a1 = 0
    elif len(tuple_a) == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if len(tuple_b) == 0:
        b0 = 0
        b1 = 0
    elif len(tuple_b) == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    new_tuple = (a0 + b0, a1 + b1)
    return new_tuple


def main():
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))


if __name__ == "__main__":
    main()
