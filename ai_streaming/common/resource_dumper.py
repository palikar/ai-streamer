import os

import numpy as np
import pandas as pd

from joblib import dump as joblib_dump


class Dumper:

    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.logger_file = os.path.join(output_dir, 'log.txt')
        with open(self.logger_file, 'w') as log:
            log.write('+----------------Log file---------------------+\n')
            log.write('|There should be some usefull information here|\n')
            log.write('+---------------------------------------------+\n\n\n')

            
        

    def dump_df(self, df, name, skip_index=True, append=False, **kwargs):
        assert(isinstance(df, pd.DataFrame))
        
        df_path = os.path.join(self.output_dir, name + ".csv")

        mode = 'w' if not append else 'a'
        
        df.to_csv(df_path,index=(not skip_index), mode=mode, **kwargs)
        
        
    def dump_array(self, arr, name, binary=False, **kwargs):
        assert(isinstance(arr, np.ndarray))

        if not binary:
            arr_path = os.path.join(self.output_dir, name + ".txt")
            np.savetxt(arr_path, arr)
        else:
            arr_path = os.path.join(self.output_dir, name + ".np")
            numpy.save(arr_path, arr)
        

        
    def dump_model_joblib(self, model, name):
        model_path = os.path.join(self.output_dir, name + ".joblib")
        joblib_dump(model, model_path)        


    def dump_log(self, string):
        with open(self.logger_file, 'a') as log:
            log.write(string + '\n')
            
    def get_logger_file(self):
        self.logger_file
        
