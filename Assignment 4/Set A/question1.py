#Write a code to read the dataset (“iris.csv”). Apply Decision Tree Classifier algorithm 
#using training criterion as entropy/ gini index and find out the accuracy of the classifier.



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\Users\\VARUN-LAP\\OneDrive\\Dokumen\\iris.csv")

X = df.drop('variety', axis=1)
y = df['variety']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

dt = DecisionTreeClassifier(criterion='entropy')

dt.fit(X_train, y_train)

y_pred = dt.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

