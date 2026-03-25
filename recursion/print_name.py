#Print name
#Problem - Print name n times using recursion

def printName(n):
    if n == 0:
        return 
    print("madhav")
    printName(n-1)

n = int(input("Enter num"))
printName(n)
