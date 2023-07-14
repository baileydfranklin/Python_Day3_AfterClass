def flattenAndSort(arr):
    # Flattens the array by concatenating all subarrays
    flattened = [num for sublist in arr for num in sublist]

    # Sorts the flattened array in ascending order
    sorted_arr = sorted(flattened)

    return sorted_arr

my_arr = [1, 10, 2, 9, 3, 8, 4, 7, 4, 5]
print(flattenAndSort([my_arr]))  # Wrapping my_arr in a list to match the expected input format
