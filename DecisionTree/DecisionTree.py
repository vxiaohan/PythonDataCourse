from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
print(clf.predict(iris.data))
tree.export_graphviz(clf, out_file='tree.dot')
