#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numer = 0
    denomin = 0
    for i in range(len(my_list)):
        numer += (my_list[i][0] * my_list[i][1])
        denomin += my_list[i][1]
    return (numer / denomin)


def main():
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))


if __name__ == "__main__":
    main()
