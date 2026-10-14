import numpy as np

two_d_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]], dtype=int)
print(two_d_array)

def access_element(array, rowIndex, columnIndex):
    if rowIndex < 0 or rowIndex >= array.shape[0] or columnIndex < 0 or columnIndex >= array.shape[1]:
        print("Incorrect index")
    else:
        print(array[rowIndex][columnIndex]) # O(1) time complexity
        
access_element(two_d_array, 2, 3)