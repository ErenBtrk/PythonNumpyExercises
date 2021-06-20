'''
22. Write a NumPy program to create a vector with values from 0 to 20
and change the sign of the numbers in the range from 9 to 15. 

'''

import numpy as np

np_vector = np.arange(0,20)

relationalVar = (np_vector >= 9) & (np_vector <=15)

np_vector[relationalVar]*=-1

print(np_vector)