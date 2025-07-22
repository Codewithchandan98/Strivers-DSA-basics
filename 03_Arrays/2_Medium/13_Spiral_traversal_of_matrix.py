

# 🌀 Spiral Traversal of a Matrix

## 📝 Problem Description

# Given an `m x n` matrix, return all elements of the matrix in **spiral order**, starting from the top-left element and moving **clockwise** inwards.


## ⚠️ Edge Cases :

# | Case Type              | Matrix                             | Output                      |
# |------------------------|-------------------------------------|-----------------------------|
# | Empty matrix           | `[]`                                | `[]`                        |
# | Single row             | `[[1, 2, 3]]`                       | `[1, 2, 3]`                 |
# | Single column          | `[[1], [2], [3]]`                   | `[1, 2, 3]`                 |
# | 1x1 matrix             | `[[7]]`                             | `[7]`                       |
# | Uneven dimensions      | `[[1,2,3], [4,5,6]]`                | `[1, 2, 3, 6, 5, 4]`        |


# ⚡ Optimal Approach (In-place Boundary Shrinking)
# 🔸 Idea
# Use 4 boundaries: top, bottom, left, right.

# Traverse edges in spiral fashion:

# Left → Right

# Top → Bottom

# Right → Left

# Bottom → Top

# Shrink boundaries after each layer.


def spiralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for col in range (left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col]) 
        bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result  

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

result = spiralOrder(matrix)
print("Sprial Traversal Output:", result)

# ⏱️ Time & Space Complexity Comparison :


# | Approach    | Time Complexity | Space Complexity | Notes                        |
# | ----------- | --------------- | ---------------- | ---------------------------- |
# | Brute Force | O(m × n)        | O(m × n)         | Uses visited matrix          |
# | Optimal     | O(m × n)        | O(1)             | No extra space except result |

# ✅ Summary
# - Use the optimal in-place boundary approach for interviews.

# - Handle edge cases: empty, 1-row, 1-col, etc.

# - Clean code with meaningful variable names (top, bottom, left, right) is key.



