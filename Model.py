import pandas as pd
import numpy as np
import Aquire
import Prepare
import Explore
import matplotlib.pyplot as plt
import seaborn as sns


import warnings 
warnings.filterwarnings('ignore')

import graphviz
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score


def train_validate_results(model, X_train, y_train, X_validate, y_validate, t_pred, v_pred,  details=False):

    '''
    this function prints the accuracy, recall and precision of the model passed in
    if details = True, it will display the classification report and the confusion matrices for train and validate dataframes
    
    '''
    print('Train model Accuracy: {:.3} % | Validate model accuracy: {:.3} % '.format(model.score(X_train, y_train) * 100, model.score(X_validate, y_validate) * 100))
    print('Train model Recall: {:.3} % | Validate model Recall: {:.3} %'.format(recall_score(y_train, t_pred) * 100, recall_score(y_validate, v_pred) * 100))
    print('Train model Precision: {:.3} % | Validate model Precision: {:.3} %'.format(precision_score(y_train, t_pred) * 100, precision_score(y_validate, v_pred) * 100))
    if details == True:
        Col_labels = ['Actual No Churn', 'Actual Churn ']
        Row_labels = ['Pred No Churn', 'Pred Churn']
        print('---------- More Details ------------')
        print('-----Train Classification report----')
        print(pd.DataFrame(classification_report(y_train, t_pred, output_dict =True)))
        print('------Validate Classification report-----')
        print(pd.DataFrame(classification_report(y_validate, v_pred, output_dict =True)))
        print('-----Train Confusion Matrix------')
        print(pd.DataFrame(confusion_matrix(t_pred, y_train), index=Row_labels, columns=Col_labels))
        print('-----Validation Confusion Matrix------')
        print(pd.DataFrame(confusion_matrix(t_pred, y_train), index=Row_labels, columns=Col_labels))




    
   