import os
import binaryornot.check as binary_check


def assert_file(file):
    if not os.path.isfile(file):
        print(f'{file} is not a file!')
    
def assert_dir(file):
    if not os.path.isdir(file):
        print(f'{file} is not a directroy!')
    

def assert_binary_file(file):
    if not binary_check.is_binary(f):
        print(f'{file} is not a binary file!')


def assert_text_file(file):
    if binary_check.is_binary(f):
        print(f'{file} is not a text file!')


def is_file_or_dir(file):
    return (os.path.isdir(file) and not os.path.isfile(file))

