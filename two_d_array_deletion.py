"""This module demonstrates how to delete elements from a two-dimensional array."""

import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)

new_two_d_array = np.delete(two_d_array, 1, axis=1) # Delete the second row (index 1)
print(new_two_d_array)

# end-of-file (EOF)