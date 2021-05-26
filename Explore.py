import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


##get univariate stats
def get_uni_stats(original_df):
    for i in original_df.columns:
        sns.histplot(data=original_df ,x = i, shrink = 0.75)
        plt.show()
        
def get_heat_map(original_df )
        