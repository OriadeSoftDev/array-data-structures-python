"""This module implements a linear search algorithm for a one-dimensional array."""

import array

my_array = array.array('i', [1,2,3,4,5])

def linear_search(values, element: int)->int:
    """Return the index of element in array, or -1 if it is not found."""
    for index, value in enumerate(values):
        if value == element:
            return index
    return -1
    
print(linear_search(my_array, 8))
