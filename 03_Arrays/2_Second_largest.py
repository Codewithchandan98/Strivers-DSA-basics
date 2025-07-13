def find_second_largest():
    arr = list(map(float, input("Enter float values: ").split()))
    if len(arr) < 2:
        print("Array should have at least 2 elements")
        return None
    
    largest = arr[0]
    second = float('-inf') 
 
    for num in arr:
        if num>largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float('-inf'):
        print("No second largest found")    
        return None
    else :
        return second        
    
print(find_second_largest())    
         
