#!/usr/bin/python3
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
        print(add(a, b))
    elif opp == "-":
        print(sub(a, b))
    elif opp == "*":
        print(mul(a, b))
    elif opp == "/":
        print(div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if __name__ == "__main__":
    main()
