# Predicting customer churn at Telco


## 1 Project Overview 
- The basis of this project is to find key drivers for churn within a given dataset. After determining what key drivers are causeing people to leave or terminate their services, we use machine learning and statistacal tests to prove that the feautures that we selected are reasons for people leaving.

## Deliverables 
- Intital rough draft Jupyter Notebook containg the thought process of determining our key drivers for churn.
- The README file that gives context to the project.
  * This readme includes key findings, take aways, and hypothesis 
- A CSV file including the customer ID, their churn and predicted churn status and their probability of churning.
- A Final Jupyter notebook containing well organized commented thought process and analysis.

## Project Summary
 - We must aquire, clean, and visualize the data in order to help narrow down true drivers for churn.
 - Models used were Logistic regression, Decision Tree, Random Forest, K-Nearesr Neighbors, all preformed well above the baseline accuracy for the MVPs.
    * MVP includes
        * Fiber optic
        * Electronic check 
        * 'monthly_charges
        * tenure
        * Two year'
        * 'None' (No Internet)
        * One Year
- I chose my random forest as it suceeds the best in recall 93.71% of the time while outpreforming the baseline accuracy by almost 10%.
- Next steps would be to find solutions to make sure our high risk customers do not churn.

## Data Dictionary
After aquireing and prepping the data, these are the variables used for the project

|  Variables             |  Definition                                |  Data Type             |
| :--------------------: | :----------------------------------------: | :--------------------: |
|  customer_id           |  unique identifier                         |  object                |
|  Gender                |  binary gender identity (0 = male 1 = female)        |  integer (boolean)     |
|  is_senior             |  senior citizen                            |  integer (boolean)     |
|  has_partner           |  significant other                         |  integer (boolean)     |
|  has_dependent         |  has dependent, dependents                 |  integer (boolean)     |
|  has_phone             |  huses phone service                       |  integer (boolean)     |
|  one_line              |  has one phone line                        |  integer (boolean)     |
|  multiple_lines        |  multiple phone lines           |  integer (boolean)     |
  |  has_internet        |  uses internet service           |  integer (boolean)     |
|  fiber optic                |  had or has fiber internet service         |  integer (boolean)     |
|  streaming_tv          |  Internet extra service                    |  integer (boolean)     |
|  streaming_movies      |  Internet extra service                    |  integer (boolean)     |
|  online_security       |  Internet extra service                    |  integer (boolean)     |
|  online_backup         |  Internet extra service                    |  integer (boolean)     |
|  device_protection     |  Internet extra service                    |  integer (boolean)     |
|  tech_support          |  Internet extra service                    |  integer (boolean)     |
|  mailed_check          |  Form of payment by mail                   |  integer (boolean)     |
|  electronic_check      |  Form of payment by E-check                |  integer (boolean)     |
|  bank_transfer         |  Form of payment by bank transfer (auto_pay)  |  integer (boolean)     |
|  credit_card           |  payment type is or was credit card (auto pay)  |  integer (boolean)     |
|  paperless_billing     |  customer bill is or was paperless         |  integer (boolean)     |
|  monthly_charges       |  current monthly charges in USD            |  float                 |
|  total_charges         |  sum of all charges for tenure in USD      |  float                 |
|  tenure                |  length of retention in months             |  integer               |
|  churn (target)        |  customer leaves company    |  integer (boolean)     |


## Process

##### Plan -> **Acquire ->** Prepare -> Explore -> Model -> Deliver
> - Store functions that are needed to acquire dat
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module
> - Complete some initial data summarization 
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> **Prepare ->** Explore -> Model -> Deliver
> - Store functions needed to prepare the iris data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> **Explore ->** Model -> Deliver
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn 
> - Run at least 2 statistical tests in data exploration.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). 
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> **Model ->** Deliver
> - Establish a baseline accuracy to determine if having a model is better well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the Aquire.py, Prepare.py, Model.py, Explore.py and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook

