def reverse_num(n):
     #checks if the num is negative
     is_negative = n < 0

     #absolute value for reversal
     n = abs(n)

     #convert the number to string, reverse it, and remove leading zeroes
     reversed_str = str(n)[::-1].lstrip('0')

     #convert back to string
     reversed_num = int(reversed_str)

     #if original number was negative make the result negative
     if is_negative:
          reversed_num = -reversed_num
     return reversed_num     
print ("before function call")
print(reverse_num(-766))