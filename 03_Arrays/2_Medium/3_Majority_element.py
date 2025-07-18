
# ✅ Problem Statement
# Given an array arr of n positive integers, find the majority element (appears more than n/2 times). If no such element exists, return -1.

# 1️⃣ Brute Force Approach (O(n²) Time | O(1) Space)

# def majority_element_brute(arr):
#     n = len(arr)
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count > n // 2:
#             return arr[i]
#     return -1
# 🔹Edge Cases Handled
# Empty array → returns -1

# No majority → returns -1

# 2️⃣ Better Approach using Hash Map (O(n) Time | O(n) Space)

# def majority_element_better(arr):
#     from collections import defaultdict
#     n = len(arr)
#     freq = defaultdict(int)

#     for num in arr:
#         freq[num] += 1
#         if freq[num] > n // 2:
#             return num

#     return -1


# 3️⃣ Optimal Approach using Moore’s Voting Algorithm (O(n) Time | O(1) Space)

def majority_element_optimal(arr):
    n = len(arr)
    if not arr:
        return -1
    
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > n // 2:
        return candidate
    else:
        return -1    

print(majority_element_optimal([3, 3, 4, 2, 3, 3, 3]))   # ➤ 3
print(majority_element_optimal([1, 2, 3, 4, 5]))         # ➤ -1
print(majority_element_optimal([2, 2, 2, 2, 2]))         # ➤ 2
print(majority_element_optimal([]))                     # ➤ -1
print(majority_element_optimal([1]))                    # ➤ 1
print(majority_element_optimal([1, 2]))                  # ➤ -1
           
