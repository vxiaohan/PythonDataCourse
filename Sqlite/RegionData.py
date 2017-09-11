import pandas
import sqlite3
df = pandas.read_csv('../Data/Region_Data.csv', encoding='gb2312', skiprows=3, skipfooter=2)
print(df.head())

df = df.melt(col_level=0 ,id_vars='地区')
df['variable'] = df['variable'].map(lambda e:int(e.split('年')[0]))
df.columns = ['area', 'year', 'gross_product']
with sqlite3.connect('country_data.sqlite') as conn:
    df.to_sql('area_data', con=conn, if_exists='replace', index=None)