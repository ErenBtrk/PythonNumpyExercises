'''
26. Write a NumPy program to find the number of rows and columns of a given matrix.

'''

import numpy as np

np_matrix = np.arange(1,21).reshape(4,5)

print(np_matrix)

print(np_matrix.shape)