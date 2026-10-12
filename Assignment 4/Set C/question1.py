#Write a code to read the dataset (“salary_data.csv”). Apply Simple Linear Regression 
#algorithm


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("C:\\Users\\VARUN-LAP\\OneDrive\\Dokumen\\salary_data.csv")

# Separate features and target
X = df[['YearsExperience']]
y = df['Salary']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Create Linear Regression model
lr = LinearRegression()

# Train the model
lr.fit(X_train, y_train)

# Predict salary
y_pred = lr.predict(X_test)

# Evaluate model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))
