'''
51. Write a NumPy program to create a new array of given shape (5,6) and type, filled with zeros. 

Given array:
[[0 0 0 0 0 0]
[0 0 0 0 0 0]
[0 0 0 0 0 0]
[0 0 0 0 0 0]
[0 0 0 0 0 0]]
New array:
[[3 0 3 0 3 0]
[7 0 7 0 7 0]
[3 0 3 0 3 0]
[7 0 7 0 7 0]
[3 0 3 0 3 0]]

'''
import numpy as np
nums = np.zeros(shape=(5, 6), dtype='int')
print("Original array:")
print(nums)
nums[::2, ::2] = 3
nums[1::2, ::2] = 7
print("\nNew array:")
print(nums)

