import array

my_array = array.array('i', [1,2,3,4,5])

def linear_search(array, element: int)->int:
    for index in range(len(array)):
        if array[index] == element:
            return index
    return -1
    
print(linear_search(my_array, 8))
