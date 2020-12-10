#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    opp = argv[2]
    if opp == "+":
        print("{} {} {} = {}".format(a, opp, b, add(a, b)))
    elif opp == "-":
        print("{} {} {} = {}".format(a, opp, b, sub(a, b)))
    elif opp == "*":
        print("{} {} {} = {}".format(a, opp, b, mul(a, b)))
    elif opp == "/":
        print("{} {} {} = {}".format(a, opp, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if __name__ == "__main__":
    main()
