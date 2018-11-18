###############################################
#########    Management Factory   #############
###############################################

class PipelineFactory(object):
    """A factory class for managing the pipeline stages. Pipeline
 stages can be registered and then they can get used by the 
with_pipeline_stage decorator.
    """
    stages = dict()

    @staticmethod
    def execute_stage(stage, model, **kwargs):
        return PipelineFactory.stages[name](model, **kwargs)

    @staticmethod
    def register_stage(name, stage_obj):
        """Register a new pipeline stage.

        :param name: The name of the stage that will be used in the 
decorator.
        :param stage_obj: A callable object that will accept a model
object and the keywords arguments passed to the with_pipeline_stage
decorator.

        """
        
        PipelineFactory.stages[name] = stage_obj


###############################################
###############################################
###############################################


###############################################
######     Models Definitions           #######
###############################################
    
