import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)
print(two_d_array)

def traverse_2d_array(array):
    for row_index, row in enumerate(array):
        for column_index, value in enumerate(row):
            print(value, end=" ")
        print()

traverse_2d_array(two_d_array) # Print a newline at the end
