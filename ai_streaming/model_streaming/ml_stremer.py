import os
import sys
import json
import numpy as np


from abc import abstractclassmethod
from abc import ABCMeta


from ..common.argument_control import Argumenter
from ..common.resource_validator import ResourceValidator


class MLStreamer(ABCMeta):
    """ An abstract base class that defines the skeleton of a process of
building a model, loading train/validate/test data and training the built model.

When the class is derived and the abstract method are implemented the 
MLStreamer.run method is to be called. The execution of the streamer loosely
 follows a pipeline execution structure. The individual steps can be summarized
as:

    1. User input definition (arg_setup)
    2. Building (model_setup) or Loading (model_load) of the model.
    3. Data Loading (load_data)
    4. Additional processing (pipeline)
    5. Training of the model (train_model)
    6. Evaluation of the model (eval_model)
    7. Saving to the ready model to storage memory (save_model)

The abstract methods can be decorated with the decorators in decorators.py.
    """

    def __init__(self):
        "docstring"
        self.argumentar =  Argumenter()
        self.resource_validation = ResourceValidator()
        self.name = None
        self.config = None
        self.lists = dict()
        self.arrays = dict()


    def get_config(self):
        """Retrieve the configuration.

        :returns: The loaded configuration in form of a dictionary.
        :rtype: dict

        """
        
        return self.config

    def get_lists(self):
        """Retrieve all of the available list files

        :returns: A dictionary of the loaded list files. 
<list file name> -> <list contents>
        :rtype: dict
        """
        
        return self.lists

    def get_arrays(self):
        """Retrieve all of the loaded array files

        :returns: A dictionary of the loaded array files. 
<array file name> -> <numpy array>
        :rtype: dict
        
        """
        return self.arrays

    
    def get_list(self, name):
        """Retrieve the contents of a list file.

        :param name: The name of the list file which contents are to be returned
        :returns: The contents of the list file in the form of a list.
        :rtype: list

        """
        
        if name not in self.lists.keys():
            print(f'{name} is not a list')
            exit(1)
        return self.lists[name]

    def get_array(self, name):
        """Retrieve the contents of an array file.

        :param name: The name of the array file which 
contents are to be returned.
        :returns: The contents of the array file in the form of a numpy array.
        :rtype: numpy.ndarray

        
        """
        if name not in self.arrays.keys():
            print(f'{name} is not a array')
            exit(1)
        return self.arrays[name]
        

    @abstractclassmethod
    def arg_setup(self, arguments):
        pass


    @abstractclassmethod
    def model_setup(self, config):#should be model_build!
        pass

        
    @abstractclassmethod
    def model_load(self, config, files):
        pass

        
    @abstractclassmethod
    def load_data(self, config, files):
        pass

        
    @abstractclassmethod
    def pipeline(self, config, model):
        pass
        
        
    @abstractclassmethod
    def train_model(self, config, data, model, pipeline):
        pass


    @abstractclassmethod
    def eval_model(self, config, data, model, pipeline):
        pass

        
    @abstractclassmethod
    def save_model(self, config, model):
        pass
    
    

    def run(self):
        """This method executes the whole process. Ideally, in your 
main function, you should only call this method on the derived class and
everything will be executed semi-automatically. The abstract methods will be
called in the appropriate places but the boilerplate code is abstracted away.
        """
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
        assert self.config is not None, 'The configuration
\file was not read properly!'
            

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
                    print(f'Could not load array file\
\'{arr_path}\' for array \'{arr_name}\'')
                    exit(1)

        # #Building the user defined model        
        model = None
        if  hasattr(args, 'model_file') and args.model_file is not None:
            model = self.model_load((args.model_file, args.weights_file))
        elif hasattr(args, 'model_dir') and args.model_dir is not None:
            model = self.model_load(args.model_dir)
        else:
            model = self.model_setup(self.config)

        assert model is not None, 'The model was not build correctly!'


        pipeline = self.pipeline(self.config, model)
        assert isinstance(pipeline, dict), "The resulting pipeline object\
 must be a dictionary!"
        
        if not args.no_train:
            #Load the data
            data = None
            if hasattr(args, 'data'):
                data = self.load_data(self.config, args.data)
            else:
                self.load_data(self, self.config,
                               (args.test, args.validate, args.train))
            assert data is not None, "The data was not properly loaded!"
            #Train model
            self.train_model(self.config, data, model, pipeline)



        if not args.no_eval:
            self.eval_model(self.config, data, model, pipeline)

        self.save_model(self.config, model)
