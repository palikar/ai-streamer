import unittest
import os

import ai_streaming.common.utils as ut

class TestDown(unittest.TestCase):

    def test_assert_file(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
        
        with self.assertRaises(AssertionError):
            ut.assert_file(test_dir)

        try:
            ut.assert_file(test_file)
        except AssertionError:
            self.fail("assert_file() raised AssertionErrorType unexpectedly!")
            

    def test_assert_dir(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        with self.assertRaises(AssertionError):
            ut.assert_dir(test_file)
        
        try:
            ut.assert_dir(test_dir)
        except AssertionError:
            self.fail("assert_dir() raised AssertionErrorType unexpectedly!")

    
    def test_assert_binary(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        binary_file = os.path.join(os.path.dirname(__file__), 'test_bin.png')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
        
        with self.assertRaises(AssertionError):
            ut.assert_binary_file(test_file)
        
        try:
            ut.assert_binary_file(binary_file)
        except AssertionError:
            self.fail("assert_binary_file() raised AssertionErrorType unexpectedly!")


    def test_assert_text(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        binary_file = os.path.join(os.path.dirname(__file__), 'test_bin.png')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
        
        with self.assertRaises(AssertionError):
            ut.assert_text_file(binary_file)
        
        try:
            ut.assert_text_file(test_file)
        except AssertionError:
            self.fail("assert_text_file() raised AssertionErrorType unexpectedly!")

    
    def test_assert_file_or_dir(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
        non_file = os.path.join(os.path.dirname(__file__), 'random.txt')
                
        with self.assertRaises(AssertionError):
            ut.assert_file_or_dir(non_file)
        
        try:
            ut.assert_file_or_dir(test_file)
        except AssertionError:
            self.fail("assert_text_file() raised AssertionErrorType unexpectedly!")
        try:
            ut.assert_file_or_dir(test_dir)
        except AssertionError:
            self.fail("assert_text_file() raised AssertionErrorType unexpectedly!")




if __name__ == '__main__':
    unittest.main()
