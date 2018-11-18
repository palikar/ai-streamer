import os
import sys
import json
import numpy as np

from abc import abstractclassmethod

from argument_control import Argumenter
from resource_validator import ResourceValidator
from model_factory import ModelFactory




class MLStreamer:
    
    def __init__(self):
        "docstring"
        self.argumentar =  Argumenter()
        self.resource_validation = ResourceValidator()
        self.name = None
        self.config = None
        self.lists = dict()
        self.arrays = dict()

    @classmethod
    def with_model_builder(cls, model=None, params=None):
        "Decoratot. Should provide different model"
        model_obj = ModelFactory.get_model(model, params)
        def decorator(fun):
            def wrapper(self, config):
                return fun(self, config, model_obj)
                pass
            return wrapper
        return decorator

    @classmethod
    def with_model_loader(cls, model=None, params=None):
        "Decoratot. Should provide different model"
        def decorator(fun):
            def wrapper(self, files):
                model_obj = ModelFactory.load_model(model, files, params)
                return fun(self,files, model_obj)
            return wrapper
        return decorator



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
    def model_setup(self, config):#should be model_build!
        "Documentation."

    
    @abstractclassmethod
    def model_load(self, files):
        "Documentation."

        
    @abstractclassmethod
    def load_data(self, files):
        "Documentation."
    

    def run(self):

        # User Input
        args = None
        self.argumentar.init(self.name)
        self.arg_setup(self.argumentar)
        self.argumentar.build()
        args = self.argumentar.parse(sys.argv[1:])
        self.argumentar.validate(args)
        assert args is not None, 'The arguments were not loaded correctly!'

        
        #Resource validation
        (files, dirs, either) = self.argumentar.get_resources(args)
        self.resource_validation.assert_resources(files, dirs, either)


        #Configuration loading

        config_file_path = os.path.abspath(args.config)
        extension = os.path.splitext(config_file_path)[1]
        if extension == ".json":
            self.config = json.load(open(config_file_path, 'r'))
        assert self.config is not None, 'The configuration file was not read properly!'
            

        # Load lists
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

        # #Building the user defined model        
        model = None
        if  hasattr(args, 'model_file') and args.model_file is not None:
            model = self.model_load((args.model_file, args.weights_file))
        elif hasattr(args, 'model_dir') and args.model_dir is not None:
            model = self.model_load(args.model_dir)
        else:
            model = self.model_setup(self.config)

        assert model is not None, 'The model was not build corecctly!'
        

        
        #Load the data

        

        
        




class TestModel(MLStreamer):


    def __init__(self):
         MLStreamer.__init__(self)
        

     
    def arg_setup(self, argumentar):
        argumentar.add_model_loader(directory=False)
        

    @MLStreamer.with_model_builder(model='keras_sequential')
    def model_setup(self, config, keras):
        
        return keras


    @MLStreamer.with_model_loader(model='keras_sequential')
    def model_load(self, files, keras):
        
        return keras
        


def main():
    TestModel().run()

if __name__ == '__main__':
    main()







    



    
        
