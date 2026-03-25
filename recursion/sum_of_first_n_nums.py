#Sum of First n nums
#Problem- Find the sum of 1st n nums using recursion

def sumOfNum(num):
    if num == 0:
        return 0 
    return num + sumOfNum(num - 1)

print(sumOfNum(5))