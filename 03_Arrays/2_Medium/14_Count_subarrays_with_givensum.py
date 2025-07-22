# 🚀 Problem: Count Subarrays with Given Sum

## 🔍 Description

# Given an array of integers `nums` and an integer `k`, return the total number of **subarrays** whose sum equals `k`.

# A subarray is a contiguous non-empty sequence of elements within an array.

# ---

## 📥 Sample Input

# nums = [1, 2, 3]
# k = 3


# ⚠️ Edge Cases :

# Negative numbers: nums = [1, -1, 0], k = 0
# Zero sum: nums = [0, 0, 0], k = 0
# Large input size (10⁵ elements)
# All elements > k or < k
# Single-element match: nums = [3], k = 3


# Approaches :

# 💀 Brute Force :
# Try all possible subarrays and count the ones whose sum is k.


# def count_subarrays_brute(nums, k):
#     n = len(nums)
#     count = 0
#     for i in range(n):
#         for j in range(i, n):
#             if sum(nums[i:j+1]) == k:
#                 count += 1
#     return count
# Time: O(n³)

# Space: O(1)



# ⚡ Better Approach (Prefix Sum without Map) :

# Precompute prefix sums and then use nested loops to find valid subarrays.


# def count_subarrays_better(nums, k):
#     n = len(nums)
#     prefix = [0] * (n + 1)
#     for i in range(n):
#         prefix[i+1] = prefix[i] + nums[i]
# 
#     count = 0
#     for i in range(n):
#         for j in range(i+1, n+1):
#             if prefix[j] - prefix[i] == k:
#                 count += 1
#     return count

# Time: O(n²)

# Space: O(n)


# 🥇 Optimal Approach (Prefix Sum + HashMap) :

# Use a running current_sum and a hashmap (prefix_sum_count) to store how many times each prefix sum has occurred.

def count_subarrays_optimal(nums, k):
    from collections import defaultdict

    count = 0
    current_sum = 0
    prefix_sum_count = defaultdict(int)

    prefix_sum_count[0] = 1

    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum_count :
            count += prefix_sum_count[current_sum - k]
        prefix_sum_count[current_sum] += 1    
    return count      

print(count_subarrays_optimal([1, 2, 3], 3))         # ➞ 2
print(count_subarrays_optimal([1, 1, 1], 2))         # ➞ 2
print(count_subarrays_optimal([1, -1, 0], 0))        # ➞ 3
print(count_subarrays_optimal([3, 4, 7, 2, -3, 1, 4, 2], 7))  # ➞ 4


# 🧾 Summary
# This is a classic prefix sum + hashmap problem.

# Practice variations:

#   - Count subarrays with at most k sum

#   - Count subarrays with sum divisible by k

#   - Count submatrices with sum = k (2D version)




