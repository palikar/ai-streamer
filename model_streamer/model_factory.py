

###############################################
#########    Management Factory   #############
###############################################

class ModelFactory(object):
    models = dict()
    loaders = dict()


    @staticmethod
    def get_model(name, params):
        return ModelFactory.models[name](params)

    
    @staticmethod
    def load_model(name, files, params):
        return ModelFactory.loaders[name](files, params)


    @staticmethod
    def register_model(name,mod):
        ModelFactory.models[name] = mod

    @staticmethod
    def register_loader(name, loader):
        ModelFactory.loaders[name] = loader


###############################################
###############################################
###############################################


###############################################
######     Models Definitions           #######
###############################################

class KerasSequential:
    def __call__(self, params):
        return "This is not kerase"

class KerasSequentialLoader:
    def __call__(self,files, params):

        if isinstance(files, tuple):
            pass
        else:
            pass

        return "This is not kerase but from file"

ModelFactory.register_model('keras_sequential', KerasSequential())
ModelFactory.register_loader('keras_sequential', KerasSequentialLoader())
    
