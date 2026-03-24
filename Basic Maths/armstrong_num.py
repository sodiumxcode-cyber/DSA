#Armstrong Num
#Problem - Check if the num is armstrong or not

def armstronNum(num):
    lenNum = len(str(num))
    ans = 0
    while num > 0:
        n = num % 10
        ans += n**lenNum
        num = num // 10
    return ans