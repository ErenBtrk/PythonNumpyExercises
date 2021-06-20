'''
57. Write a NumPy program to create a 4x4 array, now create a new array
from the said array swapping first and last, second and third columns.

'''

import numpy as np

np_matrix = np.arange(0,16).reshape(4,4)

print(np_matrix)

new_matrix = np_matrix[:,::-1]

print(new_matrix)