def find_max_consecutive_ones(nums):
    max_count = 0          # Stores the longest streak of 1s
    current_count = 0      # Tracks current streak of 1s

    for num in nums:
        if num == 1:
            current_count += 1                          # Increase current streak
            max_count = max(max_count, current_count)   # Update max if needed
        else:
            current_count = 0                           # Reset streak on 0
    return max_count

# Test case
arr = [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]  # Expected max streak = 4
print(find_max_consecutive_ones(arr))       # Output: 4
