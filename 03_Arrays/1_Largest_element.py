def check_if_sorted():
    # Take input from user and convert it to a list of integers
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    
    # Loop through array starting from index 1 to end
    for i in range(1, len(arr)):
        # If the current element is less than the previous, array is not sorted
        if arr[i] < arr[i - 1]:
            return False
    
    # If loop completes, array is sorted in non-decreasing order
    return True
