def optimized_selection_sort(arr):
    n = len(arr)
    # edge case : empty or single-element list
    if n<=1:
        return arr
    
    for i in range(n-1):
        min_index = i 
        #find the minimum element in the remaining unsorted array
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr      

my_arr = list(map(int, input("Enter the numbers separated by space: ").split()))
print(optimized_selection_sort(my_arr))