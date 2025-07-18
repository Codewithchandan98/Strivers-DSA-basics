def check_if_sorted():
    arr = list(map(int, input("Enter array elements separated by space: ").split()))  # Take input and convert to list of integers
    
    for i in range(1, len(arr)):                   # Loop from second element to end
        if arr[i] < arr[i - 1]:                    # If current element is smaller than the previous
            return False                           # Array is not sorted, return False
    
    return True                                    # If no such pair found, array is sorted

