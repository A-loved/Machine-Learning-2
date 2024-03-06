# -*- coding: utf-8 -*-
"""Multiclass Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OA-7cyhqj-0fWl35THuR1aSbLv2PW2Y6
"""

# Commented out IPython magic to ensure Python compatibility.
#importing necessary packages
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
# %matplotlib inline

#Loading the digits dataframe to digits
digits = load_digits()

dir(digits)

digits.data[0]

plt.gray()
plt.matshow(digits.images[0])

plt.gray()
for i in range(6):
    plt.matshow(digits.images[i])

digits.target[:5]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

model.predict([digits.data[6]])

model.score(x_test, y_test)

#using confusion matrix to know where the errors in prediciton occurred
y_predicted = model.predict(x_test)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_predicted)
cm

#plotting the confusion matrix graph
import seaborn as sns
plt.figure(figsize = (8,6))
sns.heatmap(cm, annot = True)
plt.xlabel('predicted')
plt.ylabel('Truth')

