def linear_search():
    arr = list(map(int, input("Enter array elements: ").split()))   # Take space-separated integers as input
    target = int(input("Enter target element: "))                   # Input the element to search for
    n = len(arr)                                                    # Get the length of the array

    if n == 0:                                                      # Edge case: empty array
        print("Array is empty.")
        return -1

    for i in range(n):                                              # Loop through the array
        if arr[i] == target:                                        # If current element matches the target
            print("Element found at index", i)                      # Print index of found element
            return i                                                # Return the index immediately

    print("Element not found.")                                     # If loop completes with no match
    return -1                                                       # Return -1 indicating not found

linear_search()                                                     # Call the function
