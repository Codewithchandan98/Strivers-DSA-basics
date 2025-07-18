
# 🔄 Rearrange Array Elements by Sign :

# 🧩 Problem Description
# You are given an integer array nums of even length, where:

# Half of the integers are positive

# Half are negative

# Your task is to rearrange the elements such that:

# Positive integers are at even indices (0, 2, 4, ...)

# Negative integers are at odd indices (1, 3, 5, ...)

# Return any valid re-arranged array that satisfies this condition.

# 🔢 Sample Input & Output

# Input:  nums = [3, 1, -2, -5, 2, -4]
# Output: [3, -2, 1, -5, 2, -4]
# Explanation:

# Positives: [3, 1, 2] → placed at indices [0, 2, 4]

# Negatives: [-2, -5, -4] → placed at indices [1, 3, 5]

# Multiple valid outputs possible.

# ⚠️ Edge Cases
# [1, -1] → ✅ Valid minimal case
# [-2, 3, -4, 1] → ✅ Already alternating
# [5, -3, -2, 4] → ✅ Random mixed order
# [3, 3, -3, -3] → ✅ Duplicates allowed if sign count is balanced

# 🚨 Brute Force Approach :
# 🧠 Logic:
# Separate the array into positives[] and negatives[]

# Fill a new array alternately with values from both lists

# 💡 Code:

# def rearrange_array_brute(nums):
#     positives = [x for x in nums if x > 0]
#     negatives = [x for x in nums if x < 0]
#     result = [0] * len(nums)
#     pos_idx, neg_idx = 0, 1
#
#     for p in positives:
#         result[pos_idx] = p
#         pos_idx += 2
#
#     for n in negatives:
#         result[neg_idx] = n
#         neg_idx += 2
#
#     return result

# ⚙️ Better Approach (Prefix Scan Based)
# This is same as brute but conceptually tries to avoid multiple passes by scanning linearly and using prefix signs or positions. (Often skipped in interviews as optimal is clean.)

# 💡 Code:

# def rearrange_array_better(nums):
#     result = [0] * len(nums)
#     pos_index, neg_index = 0, 1
#
#     for num in nums:
#         if num > 0:
#             result[pos_index] = num
#             pos_index += 2
#         else:
#             result[neg_index] = num
#             neg_index += 2
#
#     return result


# ✅ Optimal Approach (Single Pass Two-Pointer):
# ✔️ Explanation:
# Traverse nums once

# Use:

# pos_idx = 0 for placing positive numbers at even indices

# neg_idx = 1 for placing negative numbers at odd indices

# Store result in a new list of same length

# 🧾 Python Code:

def rearrange_array(nums):
    n = len(nums)
    result = [0] * n
    pos_idx, neg_idx = 0, 1

    for num in nums:
        if num > 0:
            result[pos_idx] = num
            pos_idx += 2
        else:
            result[neg_idx] = num
            neg_idx += 2

    return result

print(rearrange_array([3, 1, -2, -5, 2, -4]))  # [3, -2, 1, -5, 2, -4]
print(rearrange_array([1, -1]))               # [1, -1]
print(rearrange_array([-2, 3, -4, 1]))         # [3, -2, 1, -4]
print(rearrange_array([5, -3, -2, 4]))         # [5, -3, 4, -2]

# 🧮 Time and Space Complexity Comparison
# Approach	       Time Complexity	   Space Complexity	            Notes
# Brute Force	        O(n)	             O(n)	       Two-pass: split + merge
# Better (prefix)	    O(n)	             O(n)	       Slight improvement, still O(n) space
# Optimal	            O(n)	             O(n)	       One-pass clean, preferred in interviews

# ✅ Interview Tips
# Stick to O(n) time and O(n) space
# Avoid sorting (violates O(n))
# Don’t try to do it in-place — placing at even/odd strictly requires extra space
# Make sure to initialize the result list to the correct length
# Let me know if you want a GitHub push guide, .md file output, or to include variations like:
# Rearrange with max adjacent difference
# In-place rearrangement (if allowed)
# Different ratio of positives/negatives










