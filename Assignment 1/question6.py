# array.itemsize, array.size

import numpy as np

arr = np.array([1,7,13,105])

print("Item Size:", arr.itemsize, "bytes")

print("Total Memory:", arr.itemsize * arr.size, "bytes")
