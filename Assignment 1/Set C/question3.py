


import pandas as pd

data = pd.Series([1, 3, 5, 7, 9, 11, 13])

print("Minimum:", data.min())
print("25th Percentile:", data.quantile(0.25))
print("Median:", data.median())
print("75th Percentile:", data.quantile(0.75))
print("Maximum:", data.max())