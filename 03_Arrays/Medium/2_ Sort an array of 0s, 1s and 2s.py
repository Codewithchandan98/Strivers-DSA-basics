# Problem: Sort an array containing only 0s, 1s, and 2s without using any library sort function.

# -------------------------
# ✅ Brute Force Approach
# -------------------------
# Step 1: Count number of 0s, 1s, and 2s.
# Step 2: Overwrite the array with the correct number of 0s, then 1s, then 2s.
# Time: O(N), Space: O(N)

# def sort_colors_brute(arr):
#     count = {0: 0, 1: 0, 2: 0}
#     for num in arr:
#         count[num] += 1

#     i = 0
#     for num in [0, 1, 2]:
#         for _ in range(count[num]):
#             arr[i] = num
#             i += 1
#     return arr

# -------------------------
# ✅ Better Approach
# -------------------------
# Count 0s, 1s, and 2s without using extra map/dict.
# Time: O(N), Space: O(1)

# def sort_colors_better(arr):
#     count0 = count1 = count2 = 0
#     for num in arr:
#         if num == 0:
#             count0 += 1
#         elif num == 1:
#             count1 += 1
#         else:
#             count2 += 1

#     i = 0
#     while count0 > 0:
#         arr[i] = 0
#         i += 1
#         count0 -= 1
#     while count1 > 0:
#         arr[i] = 1
#         i += 1
#         count1 -= 1
#     while count2 > 0:
#         arr[i] = 2
#         i += 1
#         count2 -= 1

#     return arr

# -------------------------
# ✅ Optimal Approach (Dutch National Flag Algorithm)
# -------------------------
# Use 3 pointers: low, mid, and high.
# Time: O(N), Space: O(1)

def sort_colors_optimal(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# -------------------------
# ✅ Driver Code for Testing
# -------------------------
if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    print("Original array:        ", arr)
    # print("Brute Force Sorted:    ", sort_colors_brute(arr.copy()))
    # print("Better Approach Sorted:", sort_colors_better(arrcopy()))
    print("Optimal Approach Sorted:", sort_colors_optimal(arr.copy()))
