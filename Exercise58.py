'''
58. Write a NumPy program to swap rows and columns of a given array in reverse order.

'''

import numpy as np

nums = np.array([[[1, 2, 3, 4],
                 [0, 1, 3, 4],
                 [90, 91, 93, 94],
                 [5, 0, 3, 2]]]
                )

new_nums = nums[::-1,::-1]

print(new_nums)