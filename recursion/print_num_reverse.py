#Print num Reverse
#Problem- Print num from n to 1 using recursion

def printNumRev(num):
    if num == 0:
        return 
    print(num)
    printNumRev(num - 1)

printNumRev(5)