#2. Create a DataFrame from the given sample sales data:
#{
#"Product": ["Pen", "Notebook", "Chair", "Table", "Mouse", "Laptop", "Pen", 
#"Table"],
#"Price": [10, 50, 1000, 1500, 700, 55000, 10, 1500],
#"Quantity": [100, 200, 5, 2, 10, 1, 100, 2],
#"Category": ["Stationery", "Stationery", "Furniture", "Furniture", "Electronics", 
#"Electronics", "Stationery", "Furniture"]
#}

import pandas as pd

data = {
    "Product": ["Pen", "Notebook","Chair", "Table", "Mouse", "Laptop", "Pen", "Table"],
    "Price":[10, 50, 1000, 1500, 700, 55000, 10, 1500],
    "Quantity":[100, 200, 5, 2, 10, 1, 100, 2],
    "Category":["Stationery","Stationery","Furniture","Furniture","Electronics","Electronics","Stationery","Furniture"]
}

df= pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(df)

df['Category'] = df['Category'].replace('Stationery','Office Supplies')

print("\nAfter replacing category:")
print(df)

print("\nProduct count in each category:")
print(df['Category'].value_counts())

