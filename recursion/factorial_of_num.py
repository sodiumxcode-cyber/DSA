#Factorial Of a num
#Problem - Find the Factorial of a given num using recursion

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(5))