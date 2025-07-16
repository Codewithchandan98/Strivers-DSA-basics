def left_rotate():
    arr = list(map(int, input("Enter elements: ").split()))  # Take space-separated integers as input
    n = len(arr)  # Length of the array

    if n == 0:  # Edge case: empty array
        print("Empty array. Nothing to rotate.")
        return []
    if n == 1:  # Edge case: single element
        print("Only one element. No rotation needed.")
        return arr

    temp = arr[0]  # Store the first element to rotate
    for i in range(1, n):
        arr[i - 1] = arr[i]  # Shift each element one position to the left
    arr[n - 1] = temp  # Put the first element at the end

    return arr  # Return the rotated array

print(left_rotate())  # Call the function and print the result
