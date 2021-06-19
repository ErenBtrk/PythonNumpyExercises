'''
7. Write a NumPy program to test element-wise for NaN of a given array.

'''

import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))