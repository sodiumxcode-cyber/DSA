#Leetcode 1(TwoSum)

#BruteForce Approach
def SumofTarget(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


#Optimized Approach
def SumForTarget(nums, target):
    dict1 = {}
    for i, num in enumerate(nums):
        ans = target - num
        if ans in dict1:
            return [dict1[ans], i]
        dict1[num] = i