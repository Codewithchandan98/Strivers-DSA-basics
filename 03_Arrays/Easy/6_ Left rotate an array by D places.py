def left_rotate_d_times():
    arr = list(map(int, input("Enter array elements: ").split()))  # Take array input
    d = int(input("Enter number of positions to rotate: "))        # Rotation count
    n = len(arr)                                                   # Length of array

    if n == 0:                                                     # Edge case: empty array
        print("Empty array, nothing to rotate.")
        return []

    d = d % n                                                      # Normalize d if d > n

    if d == 0:                                                     # No rotation needed
        print("Rotation count is 0 or equal to array length. No rotation needed.")
        return arr

    rotated = arr[d:] + arr[:d]                                    # Slice and rotate
    return rotated                                                 # Return rotated array

print(left_rotate_d_times())                                       # Run the function
def left_rotate_d_times():
    arr = list(map(int, input("Enter array elements: ").split()))  # Take array input
    d = int(input("Enter number of positions to rotate: "))        # Rotation count
    n = len(arr)                                                   # Length of array

    if n == 0:                                                     # Edge case: empty array
        print("Empty array, nothing to rotate.")
        return []

    d = d % n                                                      # Normalize d if d > n

    if d == 0:                                                     # No rotation needed
        print("Rotation count is 0 or equal to array length. No rotation needed.")
        return arr

    rotated = arr[d:] + arr[:d]                                    # Slice and rotate
    return rotated                                                 # Return rotated array

print(left_rotate_d_times())                                       # Run the function






#to optimize this to space complexity of o(1):

def reverse(arr, start, end):
    while start < end:
        arr[start],arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_in_place():
    arr = list(map(int, input("Enter array elements: ").split()))  # Input array
    d = int(input("Enter number of positions to rotate: "))        # Rotation count
    n = len(arr)
     
    if n == 0:
        print("Empty array, nothing to rotate.")
        return []

    d = d % n  # Normalize d

    if d == 0:
        print("Rotation count is 0 or equal to array length. No rotation needed.")
        return arr

    reverse(arr, 0, d-1) 
    reverse(arr,d,n-1)
    reverse(arr,0,n-1) # reverses the entire array

    return arr

print(left_rotate_in_place())