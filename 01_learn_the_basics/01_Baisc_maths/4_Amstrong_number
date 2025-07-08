def is_amstrong(n):
    if not isinstance(n, int):
        raise TypeError("input must be an integer")
    if n < 0:
        return False
    original = n 
    num_digits = len(str(n))
    sum_of_powers = 0
    temp = n
    while temp > 0:
        digit = temp%10
        sum_of_powers += digit ** num_digits
        temp = temp//10

    return sum_of_powers == original    

print(is_amstrong(-153))
    

