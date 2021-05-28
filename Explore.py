import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


##get bivariate stats
def get_cat_stats(df):
    df = df.drop(columns = ['customer_id','tenure','monthly_charges','total_charges','internet_service_type_id', 'payment_type_id','contract_type_id'])
    for i in df.columns:
        sns.countplot(data=df, hue=i , x = 'churn') 
        plt.show()
        
def get_con_stats(df):
    df = df.drop(columns = ['senior_citizen','customer_id','gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection','tech_support','streaming_tv', 'streaming_movies', 'paperless_billing', 'One year', 'Two year', 'Fiber optic', 'None', 'Credit card (automatic)','Mailed check', 'Electronic check'])
    for i in df.columns:
        sns.histplot(data=df , x=i, hue='churn')
        plt.show()
        
def get_churn_heatmap(binary_df):
    plt.figure(figsize=(8,12))
    churn_heatmap = sns.heatmap(binary_df.corr()[['churn']].sort_values(by='churn', ascending=False), vmin=-.5, vmax=.5, annot=True)
    churn_heatmap.set_title('Feautures  Correlating with Churn')
    
    return churn_heatmap

def get_chi_test(chi_list, df, alpha):
    for i in chi_list:
        observed = pd.crosstab(df[i], df.churn)
        print(observed)
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        print('Null Hyothesis: {} does not correlate to churn'.format(i))
        print('Alternative hypothesis: {} does correlate to churn'.format(i))
        if p < alpha:
            print('p value {} is less than alpha {} , we reject our null hypothesis'.format(p,alpha))
        else:
            print('p value {} is not less than alpha {} , we  fail to reject our null hypothesis'.format(p,alpha))
        print('-------------------------------------')
        
def get_t_test(t_var, df, alpha):
    for i in t_var:
        
        
        
        
        
    
        
        