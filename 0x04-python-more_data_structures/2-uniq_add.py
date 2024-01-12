#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set(my_list)
    rem = 0
    for z in uni:
        uni += z
    return uni
