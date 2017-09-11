import pandas

m_cols = ['Time','Action','User','Product', 'Quantity','Price']
orders = pandas.read_csv('../Data/purchase_order.tab', sep='\t',parse_dates={'Dates': [0]},names=m_cols, encoding='utf-8')
orders.info()
print(orders.head())

print(orders.groupby('User')['Price'].mean())