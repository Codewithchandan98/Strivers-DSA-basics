# Kadane's Algorithm — Maximum Subarray Sum

# Problem:
# Given an integer array `nums`, find the contiguous subarray (containing at least one number) 
# with the largest sum, and return its sum.

# Examples:
# - Input: [-2,1,-3,4,-1,2,1,-5,4] → Output: 6
# - Input: [1] → Output: 1
# - Input: [-3, -2, -1] → Output: -1

# Edge Cases:
# - All negative numbers
# - Single-element array
# - Zeros in between

# Brute Force (O(n²))
# def max_subarray_brute(nums):
#     max_sum = float('-inf')
#     for i in range(len(nums)):
#         current_sum = 0
#         for j in range(i, len(nums)):
#             current_sum += nums[j]
#             max_sum = max(max_sum, current_sum)
#     return max_sum

# Better Approach (Prefix Sum, O(n²) Time | O(n) Space)
# def max_subarray_better(nums):
#     n = len(nums)
#     prefix = [0] * (n + 1)
#     for i in range(n):
#         prefix[i + 1] = prefix[i] + nums[i]
#     max_sum = float('-inf')
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             current_sum = prefix[j] - prefix[i]
#             max_sum = max(max_sum, current_sum)
#     return max_sum

# ✅ Optimal Solution (Kadane's Algorithm — O(n) Time, O(1) Space)
def max_subarray_kadane(nums):
    if not nums:
        return 0  # Handle empty input if needed

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# ✅ Test Cases
print(max_subarray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(max_subarray_kadane([1]))                            # Output: 1
print(max_subarray_kadane([-1, -2, -3]))                   # Output: -1
print(max_subarray_kadane([5, 4, -1, 7, 8]))               # Output: 23
print(max_subarray_kadane([-2, -1]))                       # Output: -1
 