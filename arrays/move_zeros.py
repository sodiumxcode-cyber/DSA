#Leetcode-283 Move Zeros
def moveZeros(nums):
    k = 0
    for i in range(0, len(nums)):
        if nums[i] != nums[k]:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
    return nums