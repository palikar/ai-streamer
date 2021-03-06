#!/usr/bin/env python3
import argparse


class Argumenter:

    def __init__(self):
        self.pareser = None
        pass


    def init(self, name, author='Stanislav Arnaudov'):
        self.data = False
        self.logging = False
        self.model_loader = False
        self.custom_files = None

        self.parser = argparse.ArgumentParser(
            prog="name",
            description=f'ML model {name}',
            epilog='Created by Stanislv Arnaudov. Built with the help of\
            AIstreamer')

        self.parser.add_argument('-nt', '--model-no-train', dest='no_train',
                                 action="store_true", required=False,
                                 default=False,
                                 help='Should the model be trained.')

        self.parser.add_argument('-ne', '--model-no-evaluate', dest='no_eval',
                                 action="store_true", required=False,
                                 default=False,
                                 help='Should the model be evaluated.')

        self.parser.add_argument('-o', '--output', dest='output',
                                 action="store", required=False,
                                 default=f'./{name}_res',
                                 help='Where the should be the results\
                                 of the executaion stored')
        
        self.parser.add_argument('-c', '--config', dest='config',
                                 action="store", required=True,
                                 help='Configuration file (config.json)')

    def get_parse_obj(self):
        return self.pareser


    def add_split_data(self):
        self.data = True
        self.parser.add_argument('-te', '--test', dest='test',action="store",
                                 required=False, default=None,
                                 help='The data to test \
                                 the final model')
        self.parser.add_argument('-tr', '--train', dest='train',action="store",
                                 required=False, default=None,
                                 help='The data to train \
                                 the model with')
        self.parser.add_argument('-v','--validate', dest='validate',
                                 action="store", required=False,
                                 default=None,
                                 help='The data to use for \
                                 validation while training.')
         

    def add_common_data(self):
        self.data = True
        self.parser.add_argument('-d','--data', dest='data', action="store",
                                 required=False, default=None,
                                 help='A single direcotry or \
                                 something to load data from. Split\
                                 will be performed later')

    def _simple_model_loader(self):
        self.parser.add_argument('-m', '--model', dest='model_file',
                                 action="store", required=False,
                                 default=-1,
                                 help='File to load the model from.')

        self.parser.add_argument('-w', '--weights', dest='weights_file',
                                 action="store", required=False,
                                 help='File to load the model weights from.')


    def _dir_model_loader(self):
        self.parser.add_argument('-md', '--model-dir', dest='model_dir',
                                 action="store", required=False,
                                 help='Direcotry for loading\
                                 model and weights')
         
        
    def add_model_loader(self, directory = False):
        self.model_loader = True
        if not directory:
            self._simple_model_loader()
        else:
            self._dir_model_loader()
            
        
    def add_custom_files(self, custom_files):
        list_help_string = ""
        self.custom_files = custom_files
        for file in custom_files:
            list_help_string += " - " + file + ' \n'
        
        self.parser.add_argument('-f', '--files', dest='custom_files', nargs='+',
                                 action="store", required=False, default=None,
                                 help=f'File to be loaded:\n\
                                 {list_help_string}.\n \
                                 The argument must be given in the form of a list\
                                 of parts of the form [< <name> <file> > ...]')

    def _simple_logging(self):
        self.parser.add_argument('--log', dest='log',
                                 action="store", required=False,
                                 choices=['silent', 'basic', 'advanced'],
                                 default='basic', help='Loggin configuration')


    def _addative_logging(self):
        self.parser.add_argument('--log', '-l', action='count', default=0,
                                 help='Logging level.')

        self.parser.add_argument('--silent', '-q', action='store_true',
                                 default=0, help='Do not log anything.')
 
        
    def add_logging(self, simple=True):
        self.logging = True
        if simple:
            self._simple_logging()
        else:
            self._addative_logging()
        

    def build(self):
        if not self.logging:
            self._simple_logging()

            
        if not self.model_loader:
            self._simple_model_loader()

            
        if not self.data:
            self.add_common_data()


    def parse(self, args_list):
        self.args = self.parser.parse_args(args_list)
        return self.args


    def _check_list(self, l, files, name):

        if len(l) == 0 and len(files) != 0:
            print(f'{name} is empty but is should\'t be')

        # print(files)
        for f in files:
            if f not in l:
                print(f'{f} is not in the {name}')
                exit(1)
            index = l.index(f)
            
            if index+1 >= len(l) or (index+1 < len(l) and l[index+1] in files):
                print('Something is wrong with {name}')
                exit(1)
        

    def validate(self, args):
        if hasattr(args, 'data'):
            if (args.data is None and args.no_train is False):
                print("You must specify --data \
when training a model")
                exit(1)

            if (args.data is None and args.no_eval is False):
                print("You must specify --data\
when evaluating a model")
                exit(1)
        else:
            if (args.test is None and
                args.no_eval is False):
                print("You must specify --test \
                when evaluating a model")
                exit(1)

            if (args.train is None and
                args.no_train is False):
                print("You must specify --train \
                when evaluating a model")
                exit(1)

        if (hasattr(args, 'model_file') and args.model_file is not -1
            and args.model_file is not None and args.weights_file is None):
            print("You've specified model file to load but no weights are given.")
            exit(1)

        if self.custom_files is not None:
            if args.custom_files is None:
                print('Files are not specified!')
                exit(1)
            self._check_list(args.custom_files, self.custom_files, "files")


    def get_custom_files(self, args):        
        files = None
        if self.custom_files is not None:
            files = zip(args.custom_files[0::2], args.custom_files[1::2])            
        return files

    def get_resources(self, args):

        files, directories, either = list(), list(), list()

        files.append(args.config)
        
        if self.custom_files is not None:
            files = files + args.custom_files[1::2]
                        
        if hasattr(args, 'data'):
            if args.data is not None: either.append(args.data)
        else:
            if args.train is not None: either.append(args.train)
            if args.test is not None: either.append(args.test)
            if args.validate is not None: either.append(args.validate)

        if hasattr(args, 'model_dir'):
            if args.model_dir is not None: directories.append(args.model_dir)
        else:
            if args.model_file != -1: files.append(args.model_file)
            if args.weights_file is not None: files.append(args.weights_file)

    
        return (files, directories, either)

        
        
