#Print Num
#Problem- Print num from 1 to n using recuriosin

def printNum(num):
    if num == 0:
        return
    
    printNum(num -1)
    print(num)

num = int(input("Enter num"))
printNum(num)