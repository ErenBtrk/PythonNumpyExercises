'''
19. Write a NumPy program to create a vector with values ranging
from 15 to 55 and print all values except the first and last.

'''

import numpy as np

np_vector = np.arange(15,55)

print(np_vector[1:-1])