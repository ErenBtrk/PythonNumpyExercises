'''
59. Write a NumPy program to multiply two given arrays of same size element-by-element. 

'''

import numpy as np

np_array1 = np.array([1,2,3,4,5])
np_array2 = np.array([2,2,2,2,2])

#np_array3 = np_array1 * np_array2
np_array3 = np.multiply(np_array1,np_array2)
print(np_array3)