



class TestModel(MLStreamer):


    def __init__(self):
         MLStreamer.__init__(self)
        

    def arg_setup(self, argumentar):
        argumentar.add_model_loader(directory=True)
        

    @MLStreamer.with_model_builder(model='keras_sequential')
    def model_setup(self, config, keras):        
        return keras


    @MLStreamer.with_model_loader(model='keras_sequential')
    def model_load(self, files, keras):
        print(f'{keras} loaded')
        return keras


    @abstractclassmethod
    def load_data(self, config, files):
        print(f'loading data from {files}')
        return "data_stuff"

    
    @abstractclassmethod
    def pipeline(self, config):
        print('Doing random shit')
        return dict({"no":"yes"})

    
    @abstractclassmethod
    def train_model(self, config, data, model, pipeline):
        print(f'training {model} with {data}')
        pass

    
    @abstractclassmethod
    def eval_model(self, config, data, model, pipeline):
        print(f'eval {model} with {data} and {pipeline}')
        pass
        
        


def main():
    TestModel().run()

if __name__ == '__main__':
    main()
