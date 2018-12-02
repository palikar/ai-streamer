import os
import sys
import json
import numpy as np


from abc import abstractclassmethod
from abc import ABCMeta


from ..common.argument_control import Argumenter
from ..common.resource_validator import ResourceValidator
from ..common.resource_dumper import Dumper


class MLStreamer():
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

    def __init__(self, name):
        "docstring"
        self.argumentar =  Argumenter()
        self.resource_validation = ResourceValidator()
        self.name = name
        self.config = None
        self.lists = dict()
        self.arrays = dict()
        self.custom_files = dict()
        self.loader = dict()
        self.dumper = None


    def get_config(self):
        """Retrieve the configuration.

        :returns: The loaded configuration in form of a dictionary.
        :rtype: dict

        """
        
        return self.config

    
    def get_custom_files(self):
        """Retrieve all of the loaded files

        :returns: A dictionary of the loaded files. 
<array file name> -> <numpy array>
        :rtype: dict 
        
        """
        return self.custom_files

    
    def get_custom_file(self, name):
        """Retrieve the object loader form a file.

        :param name: The name of the file which 
contents are to be returned.
        :returns: The contents of the array file in the form of a numpy array.
        :rtype: numpy.ndarray
        """
        #TODO: make chechek here
        return self.custom_files[name]

    
    def get_dumper(self):
        return self.dumper
        

        

    @abstractclassmethod
    def arg_setup(self, arguments):
        pass


    @abstractclassmethod
    def file_loader_setup(self, loader, config):
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

        
        if not os.path.isdir(args.output):
            os.makedirs(args.output)
        self.dumper = Dumper(args.output)


        #Configuration loading
        config_file_path = os.path.abspath(args.config)
        extension = os.path.splitext(config_file_path)[1]
        if extension == ".json":
            self.config = json.load(open(config_file_path, 'r'))
        assert self.config is not None, 'The configuration\
file was not read properly!'


        self.file_loader_setup(self.loader, self.config)
        assert self.loader is not None, "The file loader was not properly setup"
        
        # Load lists
        custom_files = self.argumentar.get_custom_files(args)
        if custom_files is not None:
            for file_name, file_path in custom_files:
                file_path = os.path.abspath(file_path)
                if file_name not in self.loader.keys():
                    print(f'No loader for file \'{file_name}\'')
                    exit(1)
                self.custom_files[file_name] = self.loader[file_name](file_path)

        # #Building the user defined model        
        model = None
        if  hasattr(args, 'model_file') and args.model_file != -1:
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
                data = self.load_data(self.config,
                               (args.train, args.validate, args.test))
            assert data is not None, "The data was not properly loaded!"
            #Train model
            self.train_model(self.config, data, model, pipeline)



        if not args.no_eval:
            self.eval_model(self.config, data, model, pipeline)

        self.save_model(self.config, model, args.output)
