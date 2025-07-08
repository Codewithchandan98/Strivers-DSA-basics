def check_palindrome(n):

    #converts the number to its absolute value
    n = abs(n)

    #reverse the given number by converting it to the string and lstrip '0'
    reversed_string = str(n)[::-1].lstrip('0')

    #convert to int and stores in reversed number
    reversed_number = int(reversed_string)

    #check if both are equal and generate the result
    if (n==reversed_number):
        print ("True")
    else :
        print ("fasle")

check_palindrome(656898)            