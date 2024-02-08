#!/usr/bin/python3


""" module for write_file """


def write_file(filename="", text=""):
    """ write file """
    with open(filename, 'w') as file:
        return file.write(text)
