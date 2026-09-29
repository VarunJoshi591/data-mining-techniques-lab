#Write a Pandas program to convert a NumPy array to a Pandas series. Sample NumPy 
#array: d1 = [10, 20, 30, 40, 50].

import numpy as np

import pandas as pd

d1 = np.array([10, 20, 30, 40, 50])

series = pd.Series(d1)

print(series)