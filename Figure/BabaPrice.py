import pandas_datareader
import matplotlib.pyplot as plt
df = pandas_datareader.DataReader('BABA', data_source='yahoo', start='2014-10-01')
df['mvg30'] = df['Close'].rolling(window=30).mean()
print(df.tail())
df[['Close', 'mvg30']].plot(kind='line')

plt.show()

df.ix[df.index >= '2017-08-01', 'Volume'].plot(kind='bar')

plt.show()