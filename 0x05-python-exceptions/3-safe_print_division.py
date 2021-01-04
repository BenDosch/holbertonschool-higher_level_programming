#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotent = a / b
    except ZeroDivisionError:
        quotent = "None"
    finally:
        print("Inside result: {}".format(quotent))
    return quotent
