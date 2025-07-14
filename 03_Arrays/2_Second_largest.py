def find_second_largest():
    arr = list(map(float, input("Enter float values: ").split()))  # Take space-separated float inputs and convert to a list
    
    if len(arr) < 2:  # Check if array has at least 2 elements
        print("Array should have at least 2 elements")
        return None
    
    largest = arr[0]                 # Initialize 'largest' as the first element
    second = float('-inf')          # Initialize 'second' as the lowest possible value (works for all floats)

    for num in arr:                 # Iterate over each number in the array
        if num > largest:           # If current number is greater than 'largest'
            second = largest        # Update 'second' to be the old 'largest'
            largest = num           # Update 'largest' to current number
        elif largest > num > second:  # If number is between 'largest' and 'second'
            second = num            # Update 'second' to current number

    if second == float('-inf'):     # If second is not updated, all elements were equal or only one unique
        print("No second largest found")    
        return None
    else:
        return second               # Return the second largest value

print(find_second_largest())        # Call the function and print the result
