###############################################
#########    Management Factory   #############
###############################################

class ModelFactory(object):
    """A factory class for managing the model loaders and builder.
Loaders and builders can be registered and then they can get used
 by the with_model_loader or with_model_builder  decorators.
    
    """
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
        return "This is keras"

class KerasSequentialLoader:
    def __call__(self,files, params):

        if isinstance(files, tuple):
            pass
        else:
            pass

        return "This is keras from files"

ModelFactory.register_model('keras_sequential', KerasSequential())
ModelFactory.register_loader('keras_sequential', KerasSequentialLoader())


###############################################
###############################################

class ScikitDecisionTreeClassificator:

    def __call__(self, params):
        from sklearn.tree import DecisionTreeClassifier
        config = params['config'] if 'config' in params.keys() else dict()
        print(config)
        tree = DecisionTreeClassifier(**config)
        return tree
        
        
class ScikitDecisionTreeClassificatorLoader:

    def __call__(self,files, params):
        
        if isinstance(files, tuple):
            model, weights = files
            
        else:
            model_dir = files

        


                

ModelFactory.register_model('scikit_tree_classifier', ScikitDecisionTreeClassificator())
ModelFactory.register_loader('scikit_tree_classifier', ScikitDecisionTreeClassificatorLoader())

###############################################
###############################################




