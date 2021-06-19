'''
12. Write a NumPy program to create an array with the values 1, 7, 13, 105
and determine the size of the memory occupied by the array.

'''

import numpy as np

np_array = np.array([1,7,13,105])
print("Original array:")
print(np_array)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (np_array.size * np_array.itemsize))