#!/usr/bin/python3


"""
function for append_write
"""


def append_write(filename="", text=""):
    """ defining append_write """
    with open(filename, 'a') as file:
        return file.write(text)
