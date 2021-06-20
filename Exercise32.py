'''
32. Write a NumPy program to compute sum of all elements,
sum of each column and sum of each row of a given array.

'''

import numpy as np

np_matrix = np.arange(0,10).reshape(5,2)
print(np_matrix)
print(np_matrix.sum())
print(np_matrix.sum(axis=0))
print(np_matrix.sum(axis=1))