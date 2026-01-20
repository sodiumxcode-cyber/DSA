#Leetcode 1480 Running Sum of 1D array
#My approach

def SumOfArray(nums):
    sum = 0
    ans = []
    for i in nums:
        sum += i
        ans.append(sum)
    return ans