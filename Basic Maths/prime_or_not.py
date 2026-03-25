#Prime Or not
#Problem- Check if the num is prime or not

import math

def primeNum(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
            break
    else:
        return True