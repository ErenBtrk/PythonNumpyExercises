'''
31. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.

'''

import numpy as np

np_matrix = np.random.randint(0,100,27).reshape(3,3,3)

print(np_matrix)