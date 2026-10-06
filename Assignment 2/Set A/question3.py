#Display only the unique values in the “department” column.
#Sample data:
#data = {
# 'name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'department': ['HR', 'IT', 'Finance', 'HR']
#}

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'department': ['HR', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

print("Unique Values:")
print(df['department'].unique())
