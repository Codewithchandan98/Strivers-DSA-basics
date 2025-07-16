# 🔹 Problem:
# Given an array of positive integers arr and a target sum target, return the indices of the two numbers such that they add up to the target.
# If no such pair exists, return [-1, -1].

# ✅ 1. Brute Force – O(n²) Time | O(1) Space
# Check every pair using two nested loops.

# def two_sum_brute(arr, target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target:
#                 return [i, j]
#     return [-1, -1]


# ✅ 2. Better Approach – O(n log n) Time | O(n) Space
# Sort + Two pointers technique
# ⚠️ Note: This does not return original indices, unless you maintain a mapping.


# def two_sum_better(arr, target):
#     indexed_arr = [(num,idx) for idx, num in enumerate(arr)]
#     indexed_arr.sort()
#     left, right = 0, len(arr) - 1

#     while left < right:
#         total = indexed_arr[left][0] + indexed_arr[right][0]
#         if total == target:
#             return [indexed_arr[left][1], indexed_arr[right][1]]
#         elif total < target:
#             left += 1
#         else : 
#             right -= 1

#     return [-1,-1]
# arr=[1,2,3,4,5,6]
# target = 7
# print(two_sum_better(arr,target))         


# ✅ 3. Optimal Approach – O(n) Time | O(n) Space
# Use a hashmap to store the required complement.

def two_sum_optimal(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return [-1,-1]
arr = [1,2,3,4,5]
target = 6
print(two_sum_optimal(arr,target))    
