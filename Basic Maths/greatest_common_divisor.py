#Greatest Common Divisor
#Problem - Find the GCD of 2 nums

def gcd(num1, num2):
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
        
    if num1 == 0:
        return num2
    return num1