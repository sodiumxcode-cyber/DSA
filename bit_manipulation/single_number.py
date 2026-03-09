#Leetcode-136 Single Numbers
#BruteForce Approach
def singleNum(nums):
    for i in range(len(nums)):
        isSingle = True

        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                isSingle = False
                break
                
        if isSingle:
            return nums[i]
    return -1

#Bit Manuplation
def sinfleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result