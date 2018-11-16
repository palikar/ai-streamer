

###############################################
#########    Management Factory   #############
###############################################

class ModelFactory(object):
    models = dict()
    @staticmethod
    def get_model(name, params):
        return ModelFactory.models[name](params)
    @staticmethod
    def register_model(name,mod):
        ModelFactory.models[name] = mod


###############################################
###############################################
###############################################


###############################################
######     Models Definitions           #######
###############################################

class KerasSequential:
    
    def configure(self, config):
        self.config = config
    def __call__(self, params):
        print("Creating keras")
        return "This is not kerase"

ModelFactory.register_model('keras_sequential', KerasSequential())
    
