def find_missing_number(arr, N):
    xor_total = 0  # XOR of all numbers from 1 to N
    xor_array = 0  # XOR of all elements in the input array

    for i in range(1, N + 1):
        xor_total ^= i       # XOR all numbers from 1 to N

    for num in arr:
        xor_array ^= num     # XOR all elements present in the array

    return xor_total ^ xor_array  # XOR of the above two gives the missing number

# Input
N = 8
arr = [1, 2, 3, 4, 6, 7, 8]       # 5 is missing

# Function call
print(find_missing_number(arr, N))  # Output: 5
