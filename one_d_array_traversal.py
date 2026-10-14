""" This module demonstrates how to traverse a one-dimensional array using the array module. """

import array

arr1 = array.array('i',[1,2,3,4,5,6])
arr2 = array.array('d',[1.3,1.5,1.6])

def traverse_array(arr):
    """Traverse the array and print each element."""
    for i in arr:
        print(i)
    print()


# traverse_array(arr1)
traverse_array(arr2)
