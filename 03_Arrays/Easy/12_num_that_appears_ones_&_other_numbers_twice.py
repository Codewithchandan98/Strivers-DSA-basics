def find_single_element(arr):
    result = 0                  # Initialize result to 0
    for num in arr:
        result ^= num           # XOR with each number (duplicates cancel out)
    return result               # Result holds the single (non-repeated) element

# Test case
mine = [1, 2, 2, 3, 3, 4, 4]     # 1 appears once, others twice
print(find_single_element(mine))  # Output: 1
