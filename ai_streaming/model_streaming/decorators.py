from .model_factory import ModelFactory
from .pipeline_factory import PipelineFactory
from .data_factory import DataFactory



def with_model_builder(model=None, **kwargs):
    """Used to decoreate the MLStreamer.model_setup method. Allows the injection

of different predifined models into the method.
    :param model: The name of the model generator to be used.
    :returns: The model object that was generated.
    :rtype:
    """
    def decorator(fun):
        def wrapper(self, config):
            model_obj = ModelFactory.get_model(model, kwargs)
            return fun(self, config, model_obj)
        return wrapper
    return decorator

def with_model_loader(model=None, **kwargs):
    """Used to decorate the MLStreamer.model_load method. Allows the easy
loading of models with the help of predefined loaders. 

    :param model: The name of the model loader to be used
    :returns: The loaded model object.
    :rtype: 
    """
    def decorator(fun):
        def wrapper(self, files):
            model_obj = ModelFactory.load_model(model, files, kwargs)
            return fun(self,files, model_obj)
        return wrapper
    return decorator


def with_data_loader(loader=None, params=None, **kwargs):
    """Used to decorate the MLStreamer.load_data method. Allows the easy
loading of data with the help of predefined loaders. 

    :param loader: The name of the loader to be used.
    :returns: The loaded data object (whatever it might be).
    :rtype: 
    """
    
    def decorator(fun):
        def wrapper(self, files):
            data = DataFactory.load(loader, files)
            return fun(self, config, files, data)
        return wrapper
    return decorator



def with_pipeline_stages(stages=None, params=None, **kwargs):
    """Used to decorate the MLStreamer.pipeline method. i

    :stages stages: An iterable of names of pipeline stages to be executed
    :returns: The results of each pipeline stage execution is put into a dict
object and injected into the function.
    :rtype: 
    
    """
    def decorator(fun):
        def wrapper(self, config, model):
            pipeline_obj = dict()
            for stage in stages:
                pipeline_obj[stage] = PipelineFactory.execute_stage(stage,
                                                                    model,
                                                                    **kwargs)
            return fun(self, config, files, data, pipeline_obj)
        return wrapper
    return decorator


