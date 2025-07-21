# 🧭 Problem: Rotate Matrix by 90 Degrees Clockwise : 

# Given an **N x N matrix**, rotate it **in-place** by **90 degrees clockwise**.

# - ✅ Must be done **in-place** (no extra matrix allowed in optimal solution).
# - ✅ Each cell's value should end up in the correct rotated position.

## 🧪 Sample Input and Output : 

### Example 1

# **Input:**
# ```python
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# **Output:**
# ```python
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

# ### Example 2

# **Input:**
# ```python
# matrix = [
#   [5, 1],
#   [2, 4]
# ]
# ```

# **Output:**
# ```python
# [
#   [2, 5],
#   [4, 1]
# ]


## ⚠️ Edge Cases

# - 1x1 matrix: Should remain unchanged.
# - Matrix with duplicate/negative values.
# - Large matrix: Efficiency matters (time and memory).
# - In-place mutation required (no return statement in optimal).

## 💡 Approaches

###  Brute Force (Using Extra Space)

# **Idea:**  
# Create a new matrix and place each element in its rotated position. Copy back to original matrix.

# **Time Complexity:** O(N²)  
# **Space Complexity:** O(N²)

# **Python Code:**

# def rotate(matrix):
#     n = len(matrix)
#     rotated = [[0]*n for _ in range(n)]  # Create a new matrix
#
#     for i in range(n):
#         for j in range(n):
#             rotated[j][n - 1 - i] = matrix[i][j]  # Place element
#
#     # Copy back to original matrix
#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = rotated[i][j]

### ⚙️ Better (Transpose + Copy Reverse)

# **Idea:**  
# Transpose the matrix, then reverse each row — but do this on a copied matrix (not in-place).

# **Time Complexity:** O(N²)  
# **Space Complexity:** O(N²)

# **Python Code:**

# def rotate(matrix):
#     n = len(matrix)
#     # Step 1: Transpose into a new matrix
#     transposed = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             transposed[i][j] = matrix[j][i]
#
#     # Step 2: Reverse each row in new matrix
#     for i in range(n):
#         matrix[i] = transposed[i][::-1]

### ⚡ Optimal (Transpose + Reverse Rows In-Place)

# **Idea:**  
# A 90° clockwise rotation = **Transpose** + **Reverse each row**, done directly in the input matrix.

# **Steps:**
# 1. **Transpose**: Swap matrix\[i\]\[j\] with matrix\[j\]\[i\] for i < j.
# 2. **Reverse**: Reverse each row.

# **Time Complexity:** O(N²)  
# **Space Complexity:** O(1) 


#### ✅ Clean Python Code (In-place & Interview-Ready)


def rotate(matrix):
    """
    Rotates the given N x N matrix by 90 degrees clockwise in-place.
    """
    n = len(matrix)

    # Step 1: Transpose (flip diagonally)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()


## 🧪 Test Case

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(matrix)

# Output:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
# for row in matrix:
#     print(row)


## 📊 Time & Space Complexity Comparison

# | Approach                  | Time Complexity | Space Complexity | In-place |
# |---------------------------|------------------|-------------------|----------|
# | Brute Force               | O(N²)            | O(N²)             | ❌       |
# | Better (copy transpose)   | O(N²)            | O(N²)             | ❌       |
# | Optimal (transpose + rev) | O(N²)            | O(1)              | ✅       |

## 🧠 Interview Tips

# - Always clarify if **in-place** rotation is required.
# - Be ready to explain the **math of index transformations**.
# - You may be asked to:
# - Rotate counter-clockwise (transpose + reverse columns).
# - Rotate 180°, 270° → apply optimal logic twice or thrice.
# - Practice dry runs to build intuition for matrix patterns.




