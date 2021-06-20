'''
50. Write a NumPy program to create a 4x4 array with random values,
now create a new array from the said array swapping first and last rows.

'''

import numpy as np

np_matrix = np.arange(1,17).reshape(4,4)

new_matrix = np_matrix[::-1]

print(np_matrix)

print(new_matrix)