'''
47. Write a NumPy program to create a one dimensional array
of forty pseudo-randomly generated values. Select random 
numbers from a uniform distribution between 0 and 1. 

'''

import numpy as np

np.random.seed(10)
print(np.random.rand(40))