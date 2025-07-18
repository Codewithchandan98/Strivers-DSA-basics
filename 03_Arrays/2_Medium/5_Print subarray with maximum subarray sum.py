
# 🧠 Problem: Maximum Subarray Sum with Indices
# 🔍 Problem Description
# Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum, and return the starting and ending indices (0-based) of that subarray, along with the sum.

# 📥 Sample Input

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 📤 Sample Output

# Start Index: 3
# End Index: 6
# Maximum Sum: 6
# Explanation: The subarray [4, -1, 2, 1] has the maximum sum = 6.

# ⚠️ Edge Cases
# All elements are negative → Return the least negative number.

# Only one element → That element is the max sum.

# Array is empty → Handle as invalid input or return (None, None, 0).

# 💡 Approach 1: Brute Force (O(N³))
# Try all subarrays using 3 nested loops.

# Calculate the sum of each and track the maximum.


# def max_subarray_brute(arr):
#     n = len(arr)
#     max_sum = float('-inf')
#     start = end = 0
#     for i in range(n):
#         for j in range(i, n):
#             current_sum = 0
#             for k in range(i, j+1):
#                 current_sum += arr[k]
#             if current_sum > max_sum:
#                 max_sum = current_sum
#                 start, end = i, j
#     return start, end, max_sum


# ⚡ Approach 2: Better (Prefix Sum) – O(N²)
# Use two nested loops and calculate sum in O(1) using prefix sums.

# def max_subarray_better(arr):
#     n = len(arr)
#     max_sum = float('-inf')
#     start = end = 0
#     prefix = [0] * (n+1)
#     for i in range(n):
#         prefix[i+1] = prefix[i] + arr[i]
#     
#     for i in range(n):
#         for j in range(i, n):
#             current_sum = prefix[j+1] - prefix[i]
#             if current_sum > max_sum:
#                 max_sum = current_sum
#                 start, end = i, j
#     return start, end, max_sum

# 🚀 Approach 3: Optimal (Kadane's Algorithm with Indices) – O(N)
#   Explanation:
# Traverse the array while maintaining:

# current_sum: Sum of current subarray.

# max_sum: Maximum sum encountered so far.

# start, end, temp_start: To track indices of the max subarray.

# ✅ Python Code:

def max_subarray_kadane(arr):
    if not arr:
        return None, None, 0

    max_sum = current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return start, end, max_sum


print(max_subarray_kadane([-2,1,-3,4,-1,2,1,-5,4]))  # (3, 6, 6)
print(max_subarray_kadane([-1, -2, -3]))             # (0, 0, -1)
print(max_subarray_kadane([5]))                     # (0, 0, 5)
print(max_subarray_kadane([]))                      # (None, None, 0)



# 📊 Time and Space Complexity :

# Approach	    Time Complexity	   Space Complexity
# Brute Force	    O(N³)	           O(1)
# Better	        O(N²)	           O(N)
# Optimal	        O(N)	           O(1)













