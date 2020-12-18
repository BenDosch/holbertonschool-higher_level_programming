#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rs = roman_string
    rn = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    num = 0
    for i in range(len(rs)):
        if i <= (len(rs) - 2) and rn[rs[i]] < rn[rs[i + 1]]:
                num += rn[rs[i + 1]] - rn[rs[i]]
        elif i >= 1 and rn[rs[i - 1]] < rn[rs[i]]:
            continue
        else:
            num += rn[rs[i]]
    return num


def main():
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))


if __name__ == "__main__":
    main()
