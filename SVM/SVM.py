from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import numpy as np
from matplotlib import pyplot as plt


def plot_estimator(estimator, x, y):
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    plt.plot()
    plt.contourf(xx, yy, z, alpha=0.4, cmap=plt.cm.RdYlBu)
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.brg)
    plt.show()


iris = load_iris()
x = iris.data[0:100, [2, 3]]
y = iris.target[0:100]
#clf1 = SVC(kernel='linear')
clf1 = SVC()
clf1.fit(x, y)
clf2 = LogisticRegression()
clf2.fit(x, y)
plot_estimator(clf1, x, y)
plot_estimator(clf2, x, y)
