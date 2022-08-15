import pandas as pd 
df = pd.read_csv("data.csv")

'''
new_df = df.dropna()
print(new_df.to_string())
'''
#dropna() delete the row which have empty cell 
'''
df.dropna(inplace = True)
print(df.to_string())
'''
#fillna()
'''
#fillna() fill the empty cell 
df.fillna(130,inplace = True)
print(df.to_string())
'''
#fillna() change in original data set 
'''
df["Calories"].fillna(130,inplace = True)
print(df.to_string())
'''
#mean()
'''
x = df["Calories"].mean()
df["Calories"].fillna(x,inplace = True)
print(df.to_string())
'''
#median()
''' 
x = df["Calories"].median()
df["Calories"].fillna(x,inplace = True)
print(df.to_string())

'''

x = df["Calories"].mode()[0]
df["Calories"].fillna(x,inplace = True)
print(df.to_string())


