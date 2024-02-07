#!/usr/bin/python3
"""
Module for reading a text file and printing its content to stdout.
"""

def read_file(filename=""):
    """
    Read the content of a text file and print it to stdout.

    """
        with open(filename, "r", encoding="utf-8") as file:
                print(line.read(), end="")
