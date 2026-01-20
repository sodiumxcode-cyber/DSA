#Leetcode 1929 Concatenation of Array

#My Approach
def Concatenate(nums):
    ans = []
    for num in nums:
        ans.append(num)
    for num in nums:
        ans.append(num)
    return ans


#Optimized Approach(using 2 pointers)
def Concatenation(nums):
    n = len(nums)
    ans = [0] * (2*n)

    for i in range(n):
        ans[i] = nums[i]
        ans[i+n] = nums[i]

    return ans