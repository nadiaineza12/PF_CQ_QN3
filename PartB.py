import math

def reduce(num, denom):
    # Check if either num or denom is zero or negative
    if num <= 0 or denom <= 0:
        return 0
    
    # Calculate the greatest common divisor
    gcd = math.gcd(num, denom)
    
    # Reduce num and denom by dividing them by the gcd
    num //= gcd
    denom //= gcd
    
    # Return 1 to indicate success
    return 1
