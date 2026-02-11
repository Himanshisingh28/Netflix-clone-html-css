import pandas as pd

s=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print(s)

# df=pd.DataFrame({"name":["himasnhi","subham","rohan"],"marks":[100,60,80]})
# print(df)
# print("this is heads")
# print(df.head)
df=pd.read_csv("annual_data.csv")
# print(df)

# print(df.head)
# print(df.tail)
# print(df.describe)
# print(df.info()) 

# data selection

print(type(df["Year"]))
print(df.iloc[1])