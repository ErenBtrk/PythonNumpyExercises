'''
20. Write a NumPy program to create a 3X4 array using and iterate over it. 

'''

import numpy as np

np_matrix = np.arange(0,12).reshape(3,4)

for row in np_matrix:
    for column in row:
        print(column) 

#############################################################

a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=" ")