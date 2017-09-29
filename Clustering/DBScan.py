import numpy as np
from PIL import Image
from sklearn.preprocessing import binarize
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

img = Image.open('../Data/handwriting.png').rotate(-90).convert('L')
data = np.array(img)
image_data = np.where(1 - binarize(data, 0) == 1)
plt.scatter(image_data[0], image_data[1], s=100, c='red', label='Cluster1')
plt.show()
X=np.column_stack([image_data[0],image_data[1]])
kmeans = KMeans(n_clusters=2,init='k-means++',random_state=42)
y_kmeans=kmeans.fit_predict(X)