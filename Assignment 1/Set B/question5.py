#Write a NumPy program to create a 3X4 array using and iterate over it

import numpy as np

arr = np.arange(12).reshape(3,4)

print("Array:")
print(arr)

print("Elements:")

for row in arr:
    for value in row:
        print(value)