'''
16. Write a NumPy program to create a 3x3 identity matrix.

'''

import numpy as np

np_matrix = np.arange(0,9).reshape(3,3)
print(np_matrix)

#########################################################

array_2D=np.identity(3)
print('3x3 matrix:')
print(array_2D)