'''
29. Write a NumPy program to create a 5x5 zero matrix with
elements on the main diagonal equal to 1, 2, 3, 4, 5.

'''

import numpy as np

np_matrix = np.zeros((5,5))
np_matrix = np.diag([1,2,3,4,5])
print(np_matrix)