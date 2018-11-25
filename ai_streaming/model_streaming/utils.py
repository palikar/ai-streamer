
import pandas as pd
import numpy as np



def fill_nan(df, column,strategy='mean'):


    if strategy == 'mean':
        df[column] = df[column].fillna(df[column].mean())
    elif strategy == 'max':
        df[column] = df[column].fillna(df[column].max())
    elif strategy == 'min':
        df[column] = df[column].fillna(df[column].min())
    elif strategy == 'drop':
        df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)    
    return df
    
