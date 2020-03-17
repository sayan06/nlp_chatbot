import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#  let's load the dataset with just a few columns and a few rows
# to speed things up

use_cols = [
    'loan_amnt', 'int_rate', 'annual_inc', 'open_acc', 'loan_status',
    
]

data = pd.read_csv(
    'loan.csv', usecols=use_cols).sample(
        10000, random_state=44)  # set a seed for reproducibility

data_show = data.head()
data_loan = data.loan_amnt.unique()
# print(data_loan)
# print(data_show)
# let's make an histogram to get familiar with the
# distribution of the variable

# fig = data.loan_amnt.hist(bins=50)
# fig.set_title('Loan Amount Requested')
# fig.set_xlabel('Loan Amount')
# fig.set_ylabel('Number of Loans')

#discrete function
data.open_acc.dropna().unique()
fig = data.open_acc.hist(bins=100)
fig.set_xlim(0, 30)
fig.set_title('Customers Annual Income')
fig.set_xlabel('Annual Income')
fig.set_ylabel('Number of Customers')
