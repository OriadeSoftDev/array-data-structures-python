import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)
print(two_d_array)

def search_element(array, target):
    for row_index, row in enumerate(array):
        for column_index, value in enumerate(row):
            if value == target:
                print(f"Element {target} found at index ({row_index}, {column_index})")
                return
    print(f"Element {target} is not found in the array")
    
search_element(two_d_array, 1)