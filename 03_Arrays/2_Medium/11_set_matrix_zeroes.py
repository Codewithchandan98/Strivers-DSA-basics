
# 🧮 Set Matrix Zeroes :

# 📝 Problem Statement
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0, in-place (i.e., modify the original matrix).

# 🔢 Sample Input and Output
# Input:

# matrix = [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 1, 1]
# ]
# Output:


# [
#   [1, 0, 1],
#   [0, 0, 0],
#   [1, 0, 1]
# ]

# ⚠️ Edge Cases :

# Matrix with no zeroes → matrix should remain unchanged.

# All elements are zero → matrix becomes all zeroes.

# Matrix with one row or one column.

# A single 0 in the matrix → sets entire row and column to 0.

# 💡 Brute Force Approach
# Idea:

# For each 0, store its row and column index.

# In a second pass, set the entire row and column to 0.

# Time Complexity: O((m×n) × (m + n))
# Space Complexity: O(m + n)


# def set_zeroes(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     zeroes = []
#     
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 zeroes.append((i, j))
#     
#     for r, c in zeroes:
#         for j in range(cols):
#             matrix[r][j] = 0
#         for i in range(rows):
#             matrix[i][c] = 0

# ⚙️ Better Approach (Using Extra Space)
# Idea:

# Use two arrays to mark the rows and columns that should be zeroed.

# Time Complexity: O(m × n)
# Space Complexity: O(m + n)


# def set_zeroes(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     row_mark = [False] * rows
#     col_mark = [False] * cols
#     
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 row_mark[i] = True
#                 col_mark[j] = True
#     
#     for i in range(rows):
#         for j in range(cols):
#             if row_mark[i] or col_mark[j]:
#                 matrix[i][j] = 0


# 🧠 Optimal Approach (In-Place Using Matrix Itself)
# ✅ Explanation:
# Use the first row and first column as markers.

# Set flags first_row_zero and first_col_zero to track if the first row/column needs to be zeroed.

# Traverse rest of the matrix and mark the first cell of the row and column if a 0 is found.

# In second pass, update the matrix accordingly.

# Finally, zero out the first row/column if needed.

# ⏱ Time Complexity: O(m × n)
# 🧠 Space Complexity: O(1)


def set_zeroes(matrix):
    m,n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j]==0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix [0][j] == 0:
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0    

matrix = [
  [1, 1, 1],
  [0, 1, 2],
  [3, 4, 5]
]
set_zeroes(matrix)
for row in matrix:
    print(row)



