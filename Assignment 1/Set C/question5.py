


import pandas as pd
import numpy as np 

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

distance = np.sqrt(np.sum((s1 - s2) **2))

print("Euclidean Distance:", distance)