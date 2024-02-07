#!/usr/bin/python3
"""
Module for reading a text file and printing its content to stdout.
"""

def read_file(filename=""):
    """
    Read the content of a text file and print it to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_file("my_file_0.txt")

