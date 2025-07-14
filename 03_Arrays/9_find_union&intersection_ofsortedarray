def union_and_intersection(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j = 0, 0
    union = []
    intersection = []

    # Main loop: traverse both arrays
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        else:  # arr1[i] == arr2[j]
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            if not intersection or intersection[-1] != arr1[i]:
                intersection.append(arr1[i])
            i += 1
            j += 1

    # Handle remaining elements in arr1
    while i < n:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    # Handle remaining elements in arr2
    while j < m:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union, intersection  # ✅ Return both lists correctly


arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6]

union, intersection = union_and_intersection(arr1, arr2)
print("Union:", union)
print("Intersection:", intersection)
