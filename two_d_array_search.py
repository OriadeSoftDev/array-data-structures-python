"""This module implements a search algorithm for a two-dimensional array using NumPy."""

import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)
print(two_d_array)

def search_element(array, target):
    """
    Search for a target in a two-dimensional array.

    Print the target's row and column indices when found, or a not-found
    message otherwise.
    """
    for row_index, row in enumerate(array):
        for column_index, value in enumerate(row):
            if value == target:
                print(f"Element {target} found at index ({row_index}, {column_index})")
                return
    print(f"Element {target} is not found in the array")
    
search_element(two_d_array, 1)
## End-of-file (EOF)