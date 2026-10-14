import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)
print(two_d_array)

# Inserting a new column at the beginning of the 2D array
new_two_d_array = np.insert(two_d_array, 0, [[1,2,3,4]], axis=1)
print(new_two_d_array)

# Inserting a new row at the beginning of the 2D array
new_two_d_array = np.insert(two_d_array, 0, [[13, 8, 6, 10]], axis=0)
print(new_two_d_array)

# Appending a row at the end of a 2D array
new_two_d_array = np.append(two_d_array, [[6,9,4,2]], axis=0)
print(new_two_d_array)

# Appending a column at the end of a 2D array
new_two_d_array = np.append(two_d_array, [[6],[7],[8],[9]], axis=1)
print(new_two_d_array)

# Appending a column to the end of an array using colum_stack() method
new_two_d_array = np.column_stack((two_d_array, np.array([6,7,8,9])))
print(new_two_d_array)