"""This module demonstrates how to access elements in a two-dimensional array."""

import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)
print(two_d_array)

def access_element(array, row_index, column_index):
    """Print the element at the specified row and column indices."""
    if row_index < 0 or row_index >= array.shape[0] or column_index < 0 or column_index >= array.shape[1]:
        print("Incorrect index")
    else:
        print(array[row_index][column_index])  # O(1) time complexity
        
access_element(two_d_array, 2, 3)

## End-of-file (EOF)
