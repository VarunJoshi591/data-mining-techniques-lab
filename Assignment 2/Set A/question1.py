#Display the first 10 rows of the dataset “employees.csv”.
#Sample data:
#data = {
#'id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Jack'],
#'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
#'salary': [50000, 60000, 55000, 65000, 70000, 62000, 58000, 69000, 61000, 57000]
#}

import pandas as pd

data = {
      'id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
      'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Jack'],
      'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
      'salary': [50000, 60000, 55000, 65000, 70000, 62000, 58000, 69000, 61000, 57000]
}

df = pd.DataFrame(data)
average_salary = df.groupby('department')['salary'].mean()
print("Average salary by department:")
print("average_salary")

filtered_employees = df[df['salary'] > 55000]
print("filtered_employess")
   
