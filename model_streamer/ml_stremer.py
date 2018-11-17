import os
import sys
import json
import numpy as np

from abc import abstractclassmethod

from argument_control import Argumenter
from resource_validator import ResourceValidator
from model_factory import ModelFactory



def with_model(model=None, params=None):
    "Decoratot. Should provide different model"
    model_obj = ModelFactory.get_model(model, params)
    def decorator(fun):
        def wrapper(self):
            fun(self, model_obj)
            pass
        return wrapper
    return decorator


class MLStreamer:
    
    def __init__(self):
        "docstring"
        self.argumentar =  Argumenter()
        self.resource_validation = ResourceValidator()
        self.name = None
        self.config = None
        self.lists = dict()
        self.arrays = dict()


    def get_config(self):
        return self.config

    def get_lists(self):
        return self.lists

    def get_arrays(self):
        return self.arrays

    
    def get_list(self, name):
        if name not in self.lists.keys():
            print(f'{name} is not a list')
            exit(1)
        return self.lists[name]

    def get_array(self, name):
        if name not in self.arrays.keys():
            print(f'{name} is not a array')
            exit(1)
        return self.arrays[name]
        

    @abstractclassmethod
    def arg_setup(self, argumentar):
        "Documentation."


    @abstractclassmethod
    def model_setup(self):
        "Documentation."        
    

    def run(self):

        # User Input
        args = None
        self.argumentar.init(self.name)
        self.arg_setup(self.argumentar)
        self.argumentar.build()
        args = self.argumentar.parse(sys.argv[1:])
        self.argumentar.validate(args)

        assert(args is not None)

        #Resource validation
        (files, dirs, either) = self.argumentar.get_resources(args)
        print(files)
        self.resource_validation.assert_resources(files, dirs, either)


        #Configuration loading
        config_file_path = os.path.abspath(args.config)
        extension = os.path.splitext(config_file_path)[1]
        if extension == "json":
            self.config = json.load(open(config_file_path, 'r'))
            


        #Load lists
        lists, arrs = self.argumentar.get_lists(args)
        if lists is not None:
            for list_name, list_path in lists:
                list_path = os.path.abspath(list_path)
                with open(list_path, 'r') as file:
                    self.lists[list_name] =  file.read().splitlines()
        if arrs is not None:
            for arr_name, arr_path in arrs:
                arr_path = os.path.abspath(arr_path)
                try:
                    self.arrays[arr_name] = np.loadtxt(arr_path)
                except ValueError:
                    print(f'Could not load array file \'{arr_path}\' for array \'{arr_name}\'')
                    exit(1)
                


        #Building the user defined model
        model = self.model_setup()

        
        




class TestModel(MLStreamer):


    def __init__(self):
         MLStreamer.__init__(self)
        

     
    def arg_setup(self, argumentar):
        argumentar.add_list_files(['images'])
        argumentar.add_array_files(['order'])
        pass

    # @with_model(model='keras_sequential')
    def model_setup(self):
        print("Yes!")
        print(self.get_arrays()['order'])
        pass



def main():
    TestModel().run()

if __name__ == '__main__':
    main()







    



    
        
