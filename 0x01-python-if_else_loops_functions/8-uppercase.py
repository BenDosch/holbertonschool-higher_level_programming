#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 124:
            up = ord(c) - 32
        else:
            up = ord(c)
        print('{:c}'.format(up), end='')
    print(''.format())
