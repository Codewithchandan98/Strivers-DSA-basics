def move_zeroes_to_end():
    arr = list(map(int, input("Enter array elements: ").split()))   # Take space-separated integers as input
    n = len(arr)                                                    # Get the length of the array

    if n == 0:                                                      # Edge case: empty array
        print("Empty array, nothing to process.")
        return []

    non_zero_index = 0                                              # Pointer to place the next non-zero element

    for i in range(n):
        if arr[i] != 0:                                             # If the current element is non-zero
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]  # Swap it to the correct position
            non_zero_index += 1                                     # Move pointer for next non-zero spot

    return arr                                                      # Return the updated array

print(move_zeroes_to_end())                                         # Call the function and print result
