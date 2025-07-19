
# 🔥 Leaders in the Array :

## 🧾 Problem Statement

# Given an array `arr[]` of size `n`, a **leader** is an element that is **greater than or equal to all the elements to its right side**.  
# The **rightmost element is always a leader**.

## 📥 Sample Input/Output:

# Input:  arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]


# 🧪 Edge Cases : 

# | Case            | Input            | Expected Output | Reason                                         |
# | --------------- | ---------------- | --------------- | ---------------------------------------------- |
# | Single element  | `[5]`            | `[5]`           | Only element is always a leader                |
# | All increasing  | `[1, 2, 3, 4]`   | `[4]`           | Only last element is leader                    |
# | All decreasing  | `[9, 8, 7, 6]`   | `[9, 8, 7, 6]`  | Every element is greater than all to its right |
# | All same        | `[4, 4, 4, 4]`   | `[4, 4, 4, 4]`  | All elements are leaders as they are equal     |
# | With duplicates | `[7, 10, 10, 5]` | `[10, 10, 5]`   | Duplicates are allowed as leaders              |


# 🚶 Brute Force Approach — O(N²):
                            
# 🔍 Logic
# For each element, iterate through all elements to its right.

# If no greater element is found, it is a leader.

# ⏱ Time Complexity: O(N²)
# 🧠 Space Complexity: O(1) (excluding output)

# 🧾 Code

# def find_leaders_brute(arr):
#     n = len(arr)
#     leaders = []
#     for i in range(n):
#         is_leader = True
#         for j in range(i + 1, n):
#             if arr[i] < arr[j]:
#                 is_leader = False
#                 break
#         if is_leader:
#             leaders.append(arr[i])
#     return leaders


# ⚡ Optimal Approach — Right-to-Left Scan — O(N) :

# 🔍 Logic

# - Traverse the array from right to left.
# - Maintain max_so_far and update it while moving left.
# - If arr[i] >= max_so_far, it's a leader.

# ⏱ Time Complexity: O(N)
# 🧠 Space Complexity: O(N) (for output list)

# ✅ Python Code (Optimal) :


def find_leaders_optimal(arr):
    n = len(arr)
    leaders = []
    max_so_far = float('-inf')

    for i in reversed(range(n)):
        if arr[i] >= max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]

    leaders.reverse()  # To maintain original left-to-right order
    return leaders

print(find_leaders_optimal([16, 17, 4, 3, 5, 2]))      # [17, 5, 2]
print(find_leaders_optimal([1, 2, 3, 4]))              # [4]
print(find_leaders_optimal([9, 8, 7, 6]))              # [9, 8, 7, 6]
print(find_leaders_optimal([5]))                      # [5]
print(find_leaders_optimal([4, 4, 4, 4]))              # [4, 4, 4, 4]
print(find_leaders_optimal([7, 10, 10, 5]))            # [10, 10, 5]

