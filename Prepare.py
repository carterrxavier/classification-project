import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


####PREP ORIGINAL DATA###
def prep_original(df):
    '''
    This function looks at the original data frame in order to do small cleaning for initial univariate visualization step. 
    drop duplicates rows or coloumns
    '''
    df = df.drop_duplicates()
    df = df.loc[:, ~df.columns.duplicated()]
    
    return df

