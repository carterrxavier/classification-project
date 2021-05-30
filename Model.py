import pandas as pd
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix,recall_score, precision_score
import warnings
warnings.filterwarnings('ignore')



def train_validate_results(model, X_train, y_train, X_validate, y_validate, details=False):

    '''
    this function prints the accuracy, recall and precision of the model passed in
    if details = True, it will display the classification report and the confusion matrices for train and validate dataframes
    
    '''
    model.fit(X_train, y_train)
    t_pred = model.predict(X_train)
    v_pred = model.predict(X_validate)
    print('Train model Accuracy: {:.5f} % | Validate model accuracy: {:.5f} % '.format(model.score(X_train, y_train) * 100, model.score(X_validate, y_validate) * 100))
    print('Train model Recall: {:.5f} % | Validate model Recall: {:.5f} %'.format(recall_score(y_train, t_pred,pos_label=0) * 100, recall_score(y_validate, v_pred, pos_label=0) * 100))
    print('Train model Precision: {:.5f} % | Validate model Precision: {:.5f} %'.format(precision_score(y_train, t_pred,pos_label=0) * 100, precision_score(y_validate, v_pred,pos_label=0) * 100))
    print('------------------------------------------------------------------------')
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
        print(pd.DataFrame(confusion_matrix(v_pred, y_validate), index=Row_labels, columns=Col_labels))

        
def test_results(model, X_test, y_test, details=False):
    model.fit(X_test, y_test)
    t_pred = model.predict(X_test)
    print('Test model Accuracy: {:.5f} %'.format(model.score(X_test, y_test) * 100))
    print('Test model Recall: {:.5f} % '.format(recall_score(y_test, t_pred,pos_label=0) * 100))
    print('Test model Precision: {:.5f} %'.format(precision_score(y_test, t_pred,pos_label=0) * 100)) 
    if details == True:
        Col_labels = ['Actual No Churn', 'Actual Churn ']
        Row_labels = ['Pred No Churn', 'Pred Churn']
        print('---------- More Details ------------')
        print('-----Test Classification report----')
        print(pd.DataFrame(classification_report(y_test, t_pred, output_dict =True)))
        print('-----Test Confusion Matrix------')
        print(pd.DataFrame(confusion_matrix(t_pred, y_test), index=Row_labels, columns=Col_labels))
        
def get_customer_predictions(model, dataframe , X_var, churn_status = None, high_risk_percentage = 0):
    
    '''
    returns highrisk customer dataframe based on there churn status and if their probability of churning is higher than the high risk percentage specified
    '''
    #establish high risk as percentage
    high_risk_percentage = high_risk_percentage * 100
    
    y_pred = model.predict(X_var)
    pred_churn_df = dataframe[['customer_id','churn']]
    proba = model.predict_proba(X_var) 
    proba_list= proba.tolist()
    churn_prob =[]
    for item in proba_list:
        churn_prob.append(item[1] * 100)
    df_prob = X_var.copy()
    pred_churn_df['churn prediction'] =  y_pred
    pred_churn_df['churn probability'] = churn_prob
    
    
    if churn_status == None:
        return pred_churn_df[pred_churn_df['churn probability'] >= high_risk_percentage]
  
    else:
        return pred_churn_df[(pred_churn_df['churn'] == churn_status) & (pred_churn_df['churn probability'] >= high_risk_percentage)]



    
   