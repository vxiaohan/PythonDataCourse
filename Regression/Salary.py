import pandas
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pandas.read_csv('../Data/Salary.csv', index_col=0)
print(df.head())
X = df[['year']]
Y = df['salary'].values

regr = LinearRegression()
regr.fit(X,Y)
print(regr.coef_, regr.intercept_)
plt.scatter(X,Y, color='black')
plt.plot(X, regr.predict(X))
poly = PolynomialFeatures(degree=2)
X_ = poly.fit_transform(X)
regr2 = LinearRegression()
regr2.fit(X_,Y)
X2 = X.sort_values(['year'])
X2_ = poly.fit_transform(X2)

plt.plot(X2, regr2.predict(X2_))

plt.show()


