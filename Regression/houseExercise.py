import pandas
from sklearn.linear_model import LinearRegression

df = pandas.read_csv('../Data/house-prices.csv')
print(df.head())
house = pandas.concat([df, pandas.get_dummies(df['Brick']), pandas.get_dummies(df['Neighborhood'])], axis=1)
del house['Neighborhood']
del house['Brick']
del house['No']
del house['West']
del house['Home']
print(house.head())
X = house[['SqFt', 'Bedrooms', 'Bathrooms', 'Offers', 'Yes', 'East', 'North']]
Y = house['Price'].values
regr = LinearRegression()
regr.fit(X,Y)
print(regr.predict(X))
