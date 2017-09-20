from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


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
x = iris.data[:,[0, 1]]
y = iris.target
clf = RandomForestClassifier(n_estimators=50, criterion='entropy')
clf.fit(x,y)
plot_estimator(clf, x, y)
