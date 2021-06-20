'''
34. Write a NumPy program to add a vector to each row of a given matrix. 

'''

import numpy as np

np_matrix = np.arange(1,13).reshape(4,3)

np_vector = np.array([1,1,0])

for item in np_matrix:
    item += np_vector

print(np_matrix)