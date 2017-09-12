from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

iris = load_iris()

x = iris.data[0:100, [2, 3]]
y = iris.target[0:100]
clf1 = SVC(kernel='linear')
clf1.fit(x, y)

clf2 = LogisticRegression()
clf2.fit(x, y)
