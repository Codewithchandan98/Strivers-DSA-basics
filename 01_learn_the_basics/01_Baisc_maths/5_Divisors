import math

def divisors(n):
    if n == 0:
        print("0 has infinite divisors (every number divides 0)")
        return

    n = abs(n)
    found = False

    # Loop only till square root of n
    for i in range(1, int(math.isqrt(n)) + 1):  # math.isqrt gives int sqrt safely
        if n % i == 0:
            print(i)  # First divisor
            if i != n // i:  # Avoid duplicate when i == n/i (like in 36: i=6)
                print(n // i)  # Second divisor
            found = True

    if not found:
        print("No proper divisors")

# Test
divisors(36)
