# ✅ 1. Brute Force (O(N³))
# Check all possible subarrays, calculate their sum, and compare it to k.

# def longest_subarray_with_sum_k_brute(arr, k):
#     n = len(arr)
#     max_len = 0

#     for i in range(n):
#         for j in range(i, n):
#             curr_sum = 0
#             for l in range(i, j + 1):
#                 curr_sum += arr[l]
#             if curr_sum == k:
#                 max_len = max(max_len, j - i + 1)
    
#     return max_len
# ✅ 2. Better (O(N²))
# Eliminate the innermost loop by maintaining a running sum for each subarray.


# def longest_subarray_with_sum_k_better(arr, k):
#     n = len(arr)
#     max_len = 0

#     for i in range(n):
#         curr_sum = 0
#         for j in range(i, n):
#             curr_sum += arr[j]
#             if curr_sum == k:
#                 max_len = max(max_len, j - i + 1)
    
#     return max_len


# #✅ 3. Optimal (O(N)) – Sliding Window (only positives)
# #If all numbers are positive, we can use a sliding window to expand and shrink based on sum.

def longest_subarray_with_sum_k_optimal(arr,k):
    n = len(arr)
    left = 0
    right = 0
    curr_sum = 0
    max_len = 0

    while right < n:
        curr_sum += arr[right]

        while curr_sum > k :
            curr_sum -= arr[left]
            left += 1

        if curr_sum ==k:
            max_len = max(max_len, right - left + 1)
        right += 1
    return max_len
arr = [1,2,2,3,4,4,5,1,1,1,1,1]
k = 5
print(longest_subarray_with_sum_k_optimal(arr,k))              