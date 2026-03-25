#Divisors of a num
#Problem- Find all the divisors of a given num

import math

def divisors(num):
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(i)
        if i != num // i:
            print(num//i)