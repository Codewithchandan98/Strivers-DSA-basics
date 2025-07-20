# # 🧩 Longest Consecutive Sequence :

# ## 📝 Problem Description

# Given an **unsorted** array of integers `nums`, return the **length of the longest consecutive elements sequence**.

# **You must solve it in O(n) time.**

# ## 📥 Sample Input & Output

# Input:  nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4].

# | Case                | Example           | Expected Output |
# | ------------------- | ----------------- | --------------- |
# | Empty array         | `[]`              | `0`             |
# | No consecutive nums | `[10, 30, 50]`    | `1`             |
# | All same            | `[7, 7, 7]`       | `1`             |
# | With duplicates     | `[1, 2, 2, 3]`    | `3`             |
# | Negative numbers    | `[-2, -1, 0, 1]`  | `4`             |
# | Already sorted      | `[1, 2, 3, 4, 5]` | `5`             |


# 🥉 Brute Force Approach – Sorting

# 🔹 Idea:
# Sort the array

# Traverse it while tracking length of consecutive sequences

# 🔹 Code :

# def longestConsecutive(nums):
#     if not nums:
#         return 0
# 
#     nums.sort()
#     longest = 1
#     current = 1
# 
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             continue  # skip duplicates
#         elif nums[i] == nums[i-1] + 1:
#             current += 1
#             longest = max(longest, current)
#         else:
#             current = 1
# 
#     return longest


# 🥈 Better Approach – Set + Brute Traversal
# 🔹 Idea:

# - Add all elements to a set

# - For each number, check if it's the start of a new sequence (num - 1 not in set)

# - Traverse the sequence using a loop

# 🔹 Code (Commented for Reference)

# def longestConsecutive(nums):
#     num_set = set(nums)
#     longest = 0
# 
#     for num in num_set:
#         if num - 1 not in num_set:
#             current = num
#             streak = 1
# 
#             while current + 1 in num_set:
#                 current += 1
#                 streak += 1
# 
#             longest = max(longest, streak)
# 
#     return longest


# 🥇 Optimal Approach – HashSet & Linear Scan ✅
# 🔹 Idea:
# - Store all values in a set for O(1) lookup

# - Only start counting a sequence if num - 1 is not in the set

# - Count the length of the sequence from there

# CODE : 

def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest

print(longestConsecutive([100, 4, 200, 1, 3, 2]))        # Output: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))          # Output: 9
print(longestConsecutive([10, 30, 50]))                   # Output: 1
print(longestConsecutive([-2, -1, 0, 1, 5, 7]))           # Output: 4
print(longestConsecutive([]))                            # Output: 0


# 🧮 Time and Space Complexity Comparison :

# | Approach                | Time Complexity | Space Complexity | Notes                   |
# | ----------------------- | --------------- | ---------------- | ----------------------- |
# | Brute Force (Sort)      | O(n log n)      | O(1) / O(n)      | Sorting-based, not O(n) |
# | Better (Set + Sequence) | O(n)            | O(n)             | Optimal and clean       |

# ✅ Final Notes :

# Always use the Set + Linear Scan approach for interviews.

# Avoid unnecessary sorting if O(n) is expected.

# Understand the importance of checking for num - 1 to avoid reprocessing.









