from sklearn.datasets import load_iris
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

iris = load_iris()
dendrogram = sch.dendrogram(sch.linkage(iris.data, method='ward'))
plt.show()
