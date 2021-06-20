'''
38. Write a NumPy program to convert a given array into bytes, and load it as array. 

'''

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
print(a)
a_bytes = a.tobytes()
a2 = np.frombuffer(a_bytes, dtype=a.dtype)
print("After loading, content of the text file:")
print(a2)
print(np.array_equal(a, a2))