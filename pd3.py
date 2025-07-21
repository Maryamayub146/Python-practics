import pandas as pd 

dataSet ={
    "Name" : ["mary","harry","charry","abc","kahlil","amir"],
    "age"  : [23,24,25,27,22,29],
    "city" : ["guj","lahr","islm","lhr","guj","dhdde"],
    "salary" : [11211,421325,14634,71334,81434,81213],
}

pdf = pd.DataFrame(dataSet)
print(pdf)
# print(pdf.info())
# print(pdf.describe())

# adding a new columns
print("after apply bonus")
pdf["bonus"] = pdf["salary"] * 0.1


# values ko update krna new values add krna
# pd.loc[row_index , "colmn name"] = new value
pdf.loc[2,"salary"] = 15634 

# multbple values add
pdf["salary"] = pdf["salary"] * 1.05
print(pdf)

# remove any col or row by using drop method
# remove multple col remove
pdf.drop(columns=["bonus","age"],inplace=True)
print(pdf)

data = pd.Series([22,33,44,55,55],index=["daye 1","day2",'day3','day4','day5'])

print(data)