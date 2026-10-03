#np.greater(), np.greater_equal(), np.less(), np.less_equal()

import numpy as np 

a = np.array([11,12,13,14,15])

b = np.array([16,17,18,19,20])

print("Greater:", np.greater(a,b)) 
print("Greater Equal:", np.greater_equal(a,b))

print("Less:", np.less(a,b))
print("Less Euqal:", np.less_equal(a,b))