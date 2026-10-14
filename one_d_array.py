""" This module demonstrates the declaration of 1-D arrays in Python. """

import array

try:
    import numpy as np
except ModuleNotFoundError:
    np = None  # pylint: disable=invalid-name

my_array = array.array('i')
print(my_array)

my_array1 = array.array('i', [1,2,3,4,5])
my_array1.insert(0,6)
print(my_array1)

if np is not None:
    np_array = np.array([], dtype=int)
    # print(np_array)
    np_array1 = np.array([1,2,3,4,5], dtype=int)
    # print(np_array1)
else:
    print("NumPy is not installed; skipping the NumPy example.")