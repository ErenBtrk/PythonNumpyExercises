'''
55. Write a NumPy program to create an array of equal shape and data type of a given array.

'''

import numpy as np
nums = np.array([[5.54, 3.38, 7.99],
                 [3.54, 8.32, 6.99],
                 [1.54, 2.39, 9.29]])

print(np.zeros_like(nums))