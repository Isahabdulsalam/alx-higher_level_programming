#!/usr/bin/python3

for number in range(0, 10):
    for comb in range(number + 1, 10):
        if number == 8 and comb == 9:
            print('89')
        else:
            print('{}{}, '.format(number, comb), end='')
