import numpy as np
import pandas as pd
from env import host, user ,password
from pydataset import data
import os

def get_connection(db, user = user, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

def get_telco_data():
    file_name = 'telco_churn.csv'
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    else:
        query = '''select *
        from  customers 
        join  contract_types 
        on	contract_types.contract_type_id = customers.contract_type_id
        join  internet_service_types 
        on internet_service_types.internet_service_type_id =
        customers.internet_service_type_id
        join  payment_types			 
        on payment_types.payment_type_id = customers.payment_type_id'''
        
        df = pd.read_sql(query,get_connection('telco_churn'))
        df.to_csv('telco_churn.csv', index=False)
        return df
        