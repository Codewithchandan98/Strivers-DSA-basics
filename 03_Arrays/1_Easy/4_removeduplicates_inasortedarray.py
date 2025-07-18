def remove_duplicates(arr):
    if not arr or len(arr) == 1:
        return len(arr)
    i = 0 
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1        


arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(arr)
print("Unique elements:", arr[:new_length])
print("New length:", new_length)

unique_array = arr[:new_length]
print("Array after removing duplicates:", unique_array)
