#1. Write a Python program to:
# a) Group by department and calculate average salary.
# b) Filter employees with salary more than 55000.

# Sample Data: 
#name department salary
#Alice HR 50000
#Bob IT 60000
#Charlie HR 55000
#David Finance 65000
#Eve IT 62000

import pandas as pd 

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
    'salary': [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

average_salary = df.groupby('department')['salary'].mean()
print("Average salary by department:")
print(average_salary)

filtered_employees = df[df['salary'] > 55000]
print("Employees with salary more than 55000:")
print(filtered_employees)