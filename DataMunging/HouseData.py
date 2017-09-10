import pandas
import numpy as np
df = pandas.read_csv("../Data/house_data.csv")
del df['Unnamed: 0']
df.ix[df['物 业 费']=='暂无资料', '物 业 费'] = np.nan
print(df.head(5))
print(df.describe())

print(df.isnull().sum()/df.count())

print(df['装修'].value_counts())

def remove_yuan(value):
    if type(value)==str:
        return value.split('元')[0]
    else:
        return value
print(df['物 业 费'].map(lambda e:e.split('元')[0] if type(e)==str else e))
