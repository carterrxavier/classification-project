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

def prep_for_model(df):
    df['total_charges'] = pd.to_numeric(df['total_charges'],errors='coerce')
    df['total_charges'].fillna(0)

    columns = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection','tech_support','streaming_tv', 'streaming_movies', 'paperless_billing', 'churn']
    for cols in columns:
        df[cols] = np.where(df[cols] == ('Yes' or 'Female'), 1, 0)

    c_type = pd.get_dummies(df.contract_type, drop_first=True)
    i_type = pd.get_dummies(df.internet_service_type, drop_first=True)
    p_type = pd.get_dummies(df.payment_type, drop_first=True)
    
    
    df = pd.concat([df,c_type,i_type,p_type] , axis=1)

      
    df = df.drop(columns=(['internet_service_type_id', 'payment_type_id','contract_type_id', 'contract_type','internet_service_type','payment_type']))
    
    
    
    return df

def telco_split(df):
    '''
    This function take in the telco_churn data acquired,
    performs a split and stratifies churn column.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=738, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=345, 
                                   stratify=train_validate.churn)
    return train, validate, test


    
    



    



    
    




        



        


    
    
    

