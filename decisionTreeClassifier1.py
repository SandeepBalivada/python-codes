from sklearn import datasets
from sklearn import metrics

from sklearn.tree import DecisionTreeClassifier

dataset = datasets.load_iris()

print("Hii sandeep\n")
model = DecisionTreeClassifier()
print(model)

print("Hii again")

model.fit(dataset.data ,dataset.target)

print(model)

expected = dataset.target
predicted = model.predict(dataset.data)

print(metrics.classification_report(expected,predicted))
print(metrics.confusion_matrix(expected,predicted)) 
