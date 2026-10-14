import array

arr1 = array.array('i',[1,2,3,4,5,6])

def access_element(array, index):
    """Access an element in the array at the specified index."""
    try:
        print(array[index])
    except IndexError:
        print(f"Index {index} is out of bounds for the array.")    


access_element(arr1,2)
