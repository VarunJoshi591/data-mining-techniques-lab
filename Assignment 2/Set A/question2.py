#2. Check if there are any missing values in the dataset and display the count per column.
#Sample data:
#data = {
# 'id': [1, 2, 3, 4],
# 'name': ['Alice', None, 'Charlie', 'David'],
# 'salary': [50000, 60000, None, 55000],
# 'department': ['HR', 'IT', 'Finance', None]
#}

import pandas as pd 

data = {
    'id': [1, 2, 3, 4],
    'name': ['Alice', None, 'Charlie', 'David'],
    'salary': [50000, 60000, None, 55000],
    'department': ['HR', 'IT', 'Finance', None]
}

df = pd.DataFrame(data)

missing_values=df.isnull().sum()

print("Missing value per column")
print(missing_values)