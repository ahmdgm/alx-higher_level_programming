#!/usr/bin/python3
"""Module: 0-read_file
function that reads a text file (UTF8) and prints it to stdout:
"""
def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        - filename: this is the file to be read
    """
    with open(filename,'r',encoding="utf-8") as file:
        file_content = file.read()
        print(file_content)
