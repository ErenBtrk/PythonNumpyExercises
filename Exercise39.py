'''
39. Write a NumPy program to convert a given list into an array,
then again convert it into a list. Check initial list and final
list are equal or not.

'''

import numpy as np

list1 = [1,2,3,4,5]

print(type(list1))

np_array = np.array(list1)

print(type(np_array))

new_list = list(np_array)

print(type(new_list))

if list1 == new_list:
    print("Initial list and final list are equal.")
else:
    print("Initial list and final list are not equal.")