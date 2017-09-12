import pandas
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pandas.read_excel('../Data/house_price_regression.xlsx')

df['age'] = df['age'].map(lambda e:2017-int(e.strip().strip('建筑年代：')))
df['direction'] = df['direction'].map(lambda e: e.strip())
df['floor_info'] = df['floor_info'].map(lambda e: e.strip())
df['layout'] = df['layout'].map(lambda e: e.strip())
df[['room', 'living_room']] = df['layout'].str.extract('(\d)室(\d)厅')
df['room'] = df['room'].astype(int)
df['living_room'] = df['living_room'].astype(int)
df['total_floor'] = df['floor_info'].str.extract('共(\d+)层')
df['total_floor'] = df['total_floor'].astype(int)
df['floor'] = df['floor_info'].str.extract('^(.)层')
del df['layout']
del df['floor_info']
del df['url']
del df['title']
df = pandas.concat([df, pandas.get_dummies(df['floor'], drop_first=True), pandas.get_dummies(df['direction'], drop_first=True)],axis=1)
del df['direction']
del df['floor']
print(df.head())

X = df[['age', 'area', 'room', 'living_room', 'total_floor', '低', '高', '东向', '南北向', '南向', '西南向', '西向']]
Y = df['price']
regr = LinearRegression()
regr.fit(X,Y)

X2 = sm.add_constant(X)
est = sm.OLS(Y, X2)
est2 = est.fit()
print(est2.summary())

