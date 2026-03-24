#Count all digits of a num
#Problem - You have to return the num of digits present in a number

def countDigit(num):
    ans = 0
    n =  0
    while num > 0:
        n = num % 10
        ans += 1
        num = num // 10
    return ans