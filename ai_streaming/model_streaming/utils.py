
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


def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)



def normalize_columns(df, columns, factor=1):
    for col in columns:
        min, max = df[col].min(), df[col].max()
        data_df[col] = factor * (data_df[col] - x_min)/(x_max - x_min)
    

    
