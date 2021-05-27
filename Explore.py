import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


##get univariate stats
def get_bi_stats(df):
    
    for i in df.columns:
        sns.countplot(data=df ,hue = i, x= df.churn)
        plt.show()
        
def get_churn_heatmap(binary_df):
    plt.figure(figsize=(8,12))
    churn_heatmap = sns.heatmap(binary_df.corr()[['churn']].sort_values(by='churn', ascending=False), vmin=-.5, vmax=.5, annot=True)
    churn_heatmap.set_title('Feautures  Correlating with Churn')
    
    return churn_heatmap
    
        