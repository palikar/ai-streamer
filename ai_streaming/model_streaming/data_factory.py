###############################################
#########    Management Factory   #############
###############################################

class DataFactory(object):
    """A factory class for managing the data loaders. Loaders
can be registered and then they can get used by the 
with_data_loader decorator.
    
    """
    loaders = dict()

    @staticmethod
    def load(loader, files, **kwargs):
        return DataFactory.loaders[name](files, kwargs)


    @staticmethod
    def register_loader(name, loader):
        """Register a new loader.

        :param name: The name of the loader that will be used in the 
decorator.
        :param stage_obj: A callable object that will accept either a
tuple of two files or a single file as well as and the
keywords arguments passed to the with_pipeline_stage decorator.
        
        """
        DataFactory.loaders[name] = loader


###############################################
###############################################
###############################################


###############################################
######         Definitions              #######
###############################################

    
