#Write a Pandas program convert the first and last character of each word to uppercase 
#in each word of a given series.

import pandas as pd

data = pd.Series(["hello", "python", "pandas", "data"])

result = data.apply(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())

print(result)

