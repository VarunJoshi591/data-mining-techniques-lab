#Write a code to read the dataset (“user_data.csv”). Apply Naïve Bayes algorithm using
#GaussianNB/ Bernoulli/ Multinomial classifier to fit training dataset and find out the 
#accuracy of the classifier.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"C:\Users\VARUN-LAP\OneDrive\Dokumen\User_Data.csv")

# Convert Gender into numeric values
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Separate input features and target
X = df.drop(['Purchased', 'User ID'], axis=1)
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

nb = GaussianNB()

nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


