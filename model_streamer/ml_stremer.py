import os
import sys
import json
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
        self.resource_validation.assert_resources(files, dirs, either)


        #Configuration loading
        # config_file_path = os.path.abspath(args.config)
        # extension = os.path.splitext(config_file_path)[1]
        # print(extension)
        # if extension == "json":
        #     self.config = json.load(open(config_file_path, 'r'))


        #Load lists
        

        #Building the user defined model
        model = self.model_setup()

        
        




class TestModel(MLStreamer):


    def __init__(self):
         MLStreamer.__init__(self)
        

     
    def arg_setup(self, argumentar):
        pass

    @with_model(model='keras_sequential')
    def model_setup(self, model):
        print("Yes!")
        print(model)
        pass



def main():
    TestModel().run()

if __name__ == '__main__':
    main()







    



    
        
