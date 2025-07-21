import pandas as pd
import numpy as np


DataSet = pd.read_csv("/Users/maryamayub/Downloads/python/Sales Data.csv",encoding="latin1")


# print(DataSet.isnull())

# remove extra colmns
DataSet.drop(columns=["Status","unnamed1"],inplace=True)

print(DataSet.describe())

# # missing value check
# print(DataSet.isnull().sum())

# add missing values 
# DataSet["Amount"].fillna(DataSet['Amount'].mean(),inplace=True )

# how to identify infinite values

# DataSet.replace([np.inf,-np.inf],np.nan,inplace=True)

# # fill the empty values
# DataFrame.fillna(DataFrame.mean(),inplace=True)

# # remove duplicate 
# DataFrame.drop_duplicates(inplace=True)

DataSet.fillna({'Amount': 0}, inplace=True)
DataSet.dropna(inplace=True)

print(f'shape:{DataSet.shape}')

# apply conditon user_id 1001132 > or age >25

apply_cond = DataSet[(DataSet["User_ID"]>1001132) & (DataSet["Age"]>35)]
print(apply_cond)

# sort the user_id

sort_value = DataSet.sort_values(by="User_ID",ascending=True)
print(sort_value)

print(DataSet.isnull().sum())

# change data type
DataSet['Amount'] = DataSet['Amount'].astype('int')
DataSet['Amount'].dtypes


# how to rename any colmns
DataSet.rename(columns={"User_ID":'Login_ID'},inplace=True)

# specific culmn py describe 
DataSet[['Age','Login_ID']].describe()

# GROUPING KRNA 
DataSet.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending = False)

print(DataSet.info())
# print(DataSet)




