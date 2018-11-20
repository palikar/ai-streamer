import unittest
import os

from ai_streaming.common.argument_control import Argumenter



class TestDown(unittest.TestCase):

    def test_no_config(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = []
        
        arg = Argumenter()
        arg.init("simple")
        arg.build()

        with self.assertRaises(SystemExit):
            parssed = arg.parse(arguments)

    def test_no_data(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.build()

        parsed = arg.parse(arguments)

        with self.assertRaises(SystemExit):
            arg.validate(parsed)

    
    def test_no_data(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir]
        
        arg = Argumenter()
        arg.init("simple")
        arg.build()

        parsed = arg.parse(arguments)
        arg.validate(parsed)

    def test_only_model(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '-m', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_model_loader(directory=False)
        arg.build()

        parsed = arg.parse(arguments)

        with self.assertRaises(SystemExit):
            arg.validate(parsed)

    
    def test_only_weights(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '-w', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_model_loader(directory=False)
        arg.build()

        parsed = arg.parse(arguments)
        arg.validate(parsed)

    def test_model_dir_1(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '-md', test_dir]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_model_loader(directory=True)
        arg.build()

        parsed = arg.parse(arguments)
        arg.validate(parsed)

        
    def test_model_dir_2(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '-m', test_dir, '-w', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_model_loader(directory=True)
        arg.build()

        with self.assertRaises(SystemExit):
            parsed = arg.parse(arguments)


    def test_list_files_1(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir,
                     '--list-files', 'list_1', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_list_files(['list_1'])
        arg.build()

        parsed = arg.parse(arguments)

    
    def test_list_files_1_no_list(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir,
                     '--list-files', 'list_1', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.build()

        with self.assertRaises(SystemExit):
            parsed = arg.parse(arguments)

    
    def test_list_files_2(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir,
                     '--list-files', 'list_2', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_list_files(['list_1'])
        arg.build()

        parsed = arg.parse(arguments)
        with self.assertRaises(SystemExit):
            arg.validate(parsed)


    def test_list_files_3(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir,
                     '--list-files', 'list_1', test_file, 'list_2']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_list_files(['list_1', 'list_2'])
        arg.build()

        parsed = arg.parse(arguments)
        
        with self.assertRaises(SystemExit):
            arg.validate(parsed)

        
    def test_list_files_4(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir,
                     '--list-files', 'list_1', test_file]
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_list_files(['list_1', 'list_2'])
        arg.build()

        parsed = arg.parse(arguments)
        
        with self.assertRaises(SystemExit):
            arg.validate(parsed)

    def test_list_files_5(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir,
                     '--list-files', 'list_1', 'list_2']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_list_files(['list_1', 'list_2'])
        arg.build()

        parsed = arg.parse(arguments)
        
        with self.assertRaises(SystemExit):
            arg.validate(parsed)

    
    def test_logging_1(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '-ll']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=False)
        arg.build()
        
        parsed = arg.parse(arguments)
        
        arg.validate(parsed)
    
    
    def test_logging_2(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '--log', 'silent']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=True)
        arg.build()
        
        parsed = arg.parse(arguments)
        
        arg.validate(parsed)

    def test_logging_3(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '-ll']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=True)
        arg.build()
        
        with self.assertRaises(SystemExit):
            parsed = arg.parse(arguments)

            
    
    
    def test_logging_4(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '--log', 'silent']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=False)
        arg.build()
        
        with self.assertRaises(SystemExit):
            parsed = arg.parse(arguments)

    def test_logging_5(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '--log', 'basic']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=True)
        arg.build()
        
        parsed = arg.parse(arguments)

    def test_logging_6(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '--log', 'advanced']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=True)
        arg.build()
        
        parsed = arg.parse(arguments)

    def test_logging_4(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')

        arguments = ['-c', test_file, '--data', test_dir, '--log', 'jiberish']
        
        arg = Argumenter()
        arg.init("simple")
        arg.add_logging(simple=True)
        arg.build()
        
        with self.assertRaises(SystemExit):
            parsed = arg.parse(arguments)
    
    def test_resource_retrieval(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
        temp = '/tmp/test.txt'

        arguments = ['-c', test_file, '--data', test_dir,
                     '-md', test_dir,
                     '--list-files', 'list_1', temp]

        arg = Argumenter()
        arg.init("simple")
        arg.add_model_loader(directory=True)
        arg.add_list_files(['list_1'])
        arg.build()

        parsed = arg.parse(arguments)

        files, dirs, both = arg.get_resources(parsed)

        
        self.assertIn(test_file, files)
        self.assertIn(temp, files)
        self.assertIn(test_dir, dirs)
        self.assertIn(test_dir, both)

    def test_list_retrieval(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_dir = os.path.join(os.path.dirname(__file__), 'test_dir')
        temp = '/tmp/test.txt'

        arguments = ['-c', test_file, '--data', test_dir,
                     '-md', test_dir,
                     '--list-files', 'list_1', temp,
                     '--array-files', 'arr_1', temp
        ]

        arg = Argumenter()
        arg.init("simple")
        arg.add_model_loader(directory=True)
        arg.add_list_files(['list_1'])
        arg.add_array_files(['arr_1'])
        arg.build()

        parsed = arg.parse(arguments)

        lists, arrays = arg.get_lists(parsed)

        self.assertIsInstance(lists, zip)
        self.assertIsInstance(arrays, zip)

        self.assertIn(('list_1', temp), lists)
        self.assertIn(('arr_1', temp), arrays)




