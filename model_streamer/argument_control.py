#!/usr/bin/env python3
import os
import sys
import argparse






class Argumenter:



    def __init__(self):
        self.pareser = None
        pass


    def init(self, name, author='Stanislav Arnaudov'):
        self.data = False
        self.logging = False
        self.model_loader = False
        
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

        self.parser.add_argument('-o', '--ouput', dest='ouput',
                                 action="store", required=False,
                                 default=f'./{name}_res',
                                 help='Where the should be the results\
                                 of the executaion stored')
        
        self.parser.add_argument('-c', '--config', dest='config',
                                 action="store", required=True,
                                 help='Configuration file (config.json)')


        

    def add_split_data(self):
        self.data = True
        self.parser.add_argument('-te', '--test', dest='test',action="store",
                                 required=False,
                                 help='The data to test \
                                 the final model')

        self.parser.add_argument('-tr', '--train', dest='train',action="store",
                                 required=False,
                                 help='The data to train \
                                 the model with')

        self.parser.add_argument('-v','--validate', dest='validate',
                                 action="store", required=False,
                                 help='The data to use for \
                                 validation while training.')
        
        

    def add_common_data(self):
        self.data = True
        self.parser.add_argument('--data', dest='data', action="store",
                                 required=False, help='A single direcotry or \
                                 something to load data from. Split\
                                 will be performed later')


    def _simple_model_loader(self):
        self.parser.add_argument('-m', '--model', dest='model_file',
                                 action="store", required=False,
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
            

        
    def add_list_files(self, list_files):
        list_help_string = ""
        self.list_files = list_files
        for list_file in list_files:
            list_help_string += " - " + list_file + ' \n'
        
        self.parser.add_argument('-l', '--list_files', dest='lists', nargs='+',
                                 action="store", required=False,
                                 help='File to load the flowing lists:\n \
                                 {list_help_string}.\n \
                                 The argument must be given in the the of list\
                                 of parts of the form [< <list> <file> > ...]')
    
    def add_array_files(self, array_files):
        list_help_string = ""
        self.arr_files = arr_files
        for arr in array_files:
            list_help_string += " - " + arr + ' \n'
        
        self.parser.add_argument('-a', '--array_files', dest='arrs', nargs='+',
                                 action="store", required=False,
                                 help='File to load the flowing arrays:\n \
                                 {list_help_string}.\n \
                                 The argument must be given in the the of list\
                                 of parts of the form [< <list> <file> > ...]')

    def _simple_logging(self):
        self.parser.add_argument('--log', dest='log',
                                 action="store", required=False,
                                 choices=['silent', 'basic', 'advanced'],
                                 default='basic', help='Loggin configuration')

    def _addative_logging(self):
        self.parser.add_argument('--logging', '-l', action='count', default=0,
                                 help='Logging level.')

        self.parser.add_argument('--silent', '-q', action='store_true',
                                 default=0, help='Do not log anything.')

        
        
    def add_logging(self, simple=True):
        self.logging = true
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

        for f in files:
            if f not in l:
                print(f'{f} is not in the {name}')
                exit(1)
            index = l.index(f)
            if l[index+1] in files:
                print('Something is wrong with {name}')
                exit(1)
        


    def validate(self, args):

        if (args.data is None and args.train is None
            and args.no_train is False):
            print("You must either specify --data or --train \
            when training a model")
            exit(1)

        if (args.data is None and args.test is None and
            args.no_eval is False):
            print("You must either specify --data or --test \
            when evaluating a model")
            exit(1)

        if (args.model_file is not None and args.weights_file is None
            and args.model_dir):
            print("You've specified model file to load bu no weights are given.")
            exit(1)

        if self.list_files is not None:
            self._check_list(args.lists)

        if self.arr_files is not None:
            self._check_list(args.arrs)

    def get_resources(self, args):

        files, directories, either = list(), list(), list()

        



        return (files, directories, either)
        

            
            


def main():
    ar = Argumenter()
    ar.init("MLawesome")
    ar.build()
    ar.parse(sys.argv)
    pass
    
        
if __name__ == '__main__':
    main()
        

        

        

        
    
    
