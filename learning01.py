import numpy as np

# Create an array
arr = np.array([69, 420, 69420])

# Print the nth element
print(arr[0])

# Multi-dimensional array
dimensional_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Copy Array
arr_copy = arr.copy()
print(arr, arr_copy) # Prints the same values!
arr_copy[0] = 32
print(arr, arr_copy) # Prints arrays with different 0th index values!

# View Array
arr_view = arr.view()
print(arr, arr_view)
arr_view[0] = 120
print(arr, arr_view)
