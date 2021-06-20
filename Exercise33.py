'''
33. Write a NumPy program to compute the inner product of two given vectors.

'''

import numpy as np

np_vector1 = np.array([1,2,3,4,5])
np_vector2 = np.array([5,4,3,2,1])

print("Inner product of said vectors:")
print(np.dot(np_vector1, np_vector2))