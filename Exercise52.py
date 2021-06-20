'''
52. Write a NumPy program to sort a given array by row and column in ascending order.

'''

import numpy as np

nums = np.array([[5.54, 3.38, 7.99],
                 [3.54, 4.38, 6.99],
                 [1.54, 2.39, 9.29]])
print("By Row:")
print(np.sort(nums,axis=0))
print("By Column:")
print(np.sort(nums,axis=1))


