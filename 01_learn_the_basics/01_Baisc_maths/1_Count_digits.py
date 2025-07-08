def c_digits(n):
        if not isinstance(n, int):                              #if the input is not an integer, rasie an alert to the user
              raise TypeError("Input must be an integer")
        n = abs(n)                                              #convert the number to its abosulte value, if its negative
        if n == 0:                                              
           return 1                                             #return 1 if the number is 0, - edge case        
        count = 0
        while(n>0):
                n = n//10
                count +=1
        return count
print(c_digits(-676767))                


