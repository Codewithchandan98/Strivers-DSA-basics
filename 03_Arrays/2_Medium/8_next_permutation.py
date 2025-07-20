
# ❌ Brute Force Approach
# - Generate all permutations, sort them, and return the next one.
# - Not efficient at all, only for academic purposes.


# Brute force: Generate, sort, and find next
# from itertools import permutations

# def next_permutation(nums):
#     perms = sorted(set(permutations(nums)))
#     for i in range(len(perms)):
#         if list(perms[i]) == nums:
#             return list(perms[(i+1)%len(perms)])
# ⏱️ Time: O(N! * N)
# 📦 Space: O(N!)


# ✅ Optimal Approach (In-place) :

# Steps:
# - Traverse from end to find first decreasing element: nums[i] < nums[i+1].
# - Find the smallest element on right of i that is greater than nums[i], call it j.
# - Swap nums[i] and nums[j].
# - Reverse the suffix starting from i+1.



# Clean python code :


def next_permutation(nums):
   n = len(nums)

   i = n - 2
   while i >= 0 and nums[i] >= nums[i+1]:
      i -= 1

   
   if i > = 0:
      
      j = n - 1
      while nums[j] <= nums [i]:
         j -= 1
         nums[i], nums[j] = nums[j], nums[i]

   left, right = i + 1, n - 1
   while left < right:
      nums[left], nums[right] = nums[right] , nums[left]
      left += 1
      right -= 1    

# Test 1
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # Output: [1, 3, 2]

# Test 2
nums = [3, 2, 1]
next_permutation(nums)
print(nums)  # Output: [1, 2, 3]

# Test 3
nums = [1, 1, 5]
next_permutation(nums)
print(nums)  # Output: [1, 5, 1]

# Test 4
nums = [1, 3, 2]
next_permutation(nums)
print(nums)  # Output: [2, 1, 3]


# ⏱️ Time and Space Complexity
# Approach	Time Complexity	  Space Complexity	    In-Place	         Notes
# Brute Force	   O(N! * N)	       O(N!)	           ❌	   Generates all permutations
# Optimal	         O(N)	            O(1)	           ✅	   Efficient and required in interviews

# 📌 Interviewer Checklist :

# ✅ Solves in-place
# ✅ Lexicographical understanding
# ✅ Handles duplicates and descending cases
# ✅ Uses two-pointer approach cleanly
# ✅ Handles edge cases gracefully

# 📦 Summary
# - Pattern: Two-pointer, greedy, in-place rearrangement.
# -Applications: Next lexicographical string, permutations of strings/numbers, optimization steps.
# -Must-Know: Asked in many top company interviews — Google, Amazon, Facebook, etc.



         