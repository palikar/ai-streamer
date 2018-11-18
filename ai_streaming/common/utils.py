import os
import binaryornot.check as binary_check


def assert_file(file):
    assert os.path.isfile(file) is True, f'{file} is not a file!'

    
def assert_dir(file):
    assert os.path.isdir(file), f'{file} is not a directroy!'
            

def assert_binary_file(file):
    assert binary_check.is_binary(f), f'{file} is not a binary file!'
        

def assert_text_file(file):
    assert binary_check.is_binary(f), f'{file} is not a text file!'

    
def is_file_or_dir(file):
    return (os.path.isdir(file) and not os.path.isfile(file))

