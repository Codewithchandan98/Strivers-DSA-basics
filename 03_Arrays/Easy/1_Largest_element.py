def find_largest_element():
    arr = list(map(int, input("Enter array elements separated by space: ").split()))  # Read input as a list of integers
    
    if not arr:                          # Check if the array is empty
        print("Array is empty.")        
        return None                      # Return None if no elements
    
    largest = arr[0]                     # Initialize largest with the first element
    
    for i in range(1, len(arr)):         # Loop through the array starting from index 1
        if arr[i] > largest:             # If current element is greater than largest so far
            largest = arr[i]             # Update largest
    
    return largest                       # Return the final largest element

# Driver code to test the function
if __name__ == "__main__":
    result = find_largest_element()     # Call the func
