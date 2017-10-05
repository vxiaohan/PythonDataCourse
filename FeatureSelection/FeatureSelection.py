import pandas
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

df = pandas.read_csv('../Data/customer_behavior.csv')
x = df[['bachelor','gender','age','salary']]
y=df['purchased'].values
sel=VarianceThreshold()
x_val = sel.fit_transform(x)
print(x_val)
print(sel.get_support())


clf=SelectKBest(chi2,k=2)
clf.fit(x,y)
x_new = clf.fit_transform(x,y)
print(clf.scores_)
print(x_new)