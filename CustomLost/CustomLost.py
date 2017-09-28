import pandas
from sklearn import tree
from IPython.display import Image

df = pandas.read_csv('../Data/customer_churn.csv', index_col=0, header=0)
df = df.ix[:, 3:]

cat_var = ['international_plan', 'voice_mail_plan', 'churn']
for var in cat_var:
    df[var] = df[var].map(lambda e: 1 if e == 'yes' else 0)

y = df.ix[:, -1]
x = df.ix[:, :-1]
print(df.head())
print(df.info())

clf = tree.DecisionTreeClassifier(max_depth=5)
clf.fit(x,y)
tree.export_graphviz(clf,out_file='tree.dot')
Image('tree.png')
