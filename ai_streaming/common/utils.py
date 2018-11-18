import os
import binaryornot.check as binary_check


def assert_file(file):
    assert (os.path.isfile(file) and
            not os.path.isdir(file)), f'{file} is not a file!'

    
def assert_dir(file):
    assert os.path.isdir(file), f'{file} is not a directroy!'
            

def assert_binary_file(file):
    assert_file(file)
    assert binary_check.is_binary(file), f'{file} is not a binary file!'
        

def assert_text_file(file):
    assert_file(file)
    assert not binary_check.is_binary(file), f'{file} is not a text file!'


def is_file_or_dir(file):
    return (os.path.isdir(file) or os.path.isfile(file))


def assert_file_or_dir(file):
    assert is_file_or_dir(file), f'{file} is neither file nor directroy'
