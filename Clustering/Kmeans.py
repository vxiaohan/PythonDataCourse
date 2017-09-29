from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=500, random_state=123)

y_kmeans = kmeans.fit_predict(iris.data)
print(y_kmeans)

plt.scatter(iris.data[y_kmeans == 0, 2], iris.data[y_kmeans == 0, 3], s=100, c='red', label='Cluster1')
plt.scatter(iris.data[y_kmeans == 1, 2], iris.data[y_kmeans == 1, 3], s=100, c='blue', label='Cluster2')
plt.scatter(iris.data[y_kmeans == 2, 2], iris.data[y_kmeans == 2, 3], s=100, c='green', label='Cluster3')
plt.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:, 3], s=100, c='yellow', label='centers')
plt.show()
