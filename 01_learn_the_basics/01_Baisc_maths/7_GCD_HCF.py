def gcd(a, b):
    # Handle edge case: both zero
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both numbers zero")
    
    a, b = abs(a), abs(b)  # Use absolute values
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(98,44))