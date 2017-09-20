from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

digits = load_digits()
scaler = StandardScaler()
scaler.fit(digits.data)
X_scaled = scaler.transform(digits.data)
mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30), activation='logistic', max_iter=300)
mlp.fit(X_scaled, digits.target)

predicted = mlp.predict(X_scaled)
fig = plt.figure(figsize=(8, 8))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(36):
    ax = fig.add_subplot(6, 6, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str('{}-{}'.format(digits.target[i], predicted[i])), color='red', fontsize=20)
plt.show()

correct_count = 0
for a, b in zip(digits.target, predicted):
    if a == b:
        correct_count += 1
print('correct:' + str(correct_count))
print('total:' + str(len(predicted)))
print(correct_count / len(predicted))
