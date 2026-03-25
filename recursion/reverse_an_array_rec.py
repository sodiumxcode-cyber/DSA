#Reverse an arraya using recursion

def revArray(nums, left, right):
    if left >= right:
        return 
    
    nums[left], nums[right] = nums[right], nums[left]

    revArray(nums, left + 1, right - 1)

nums = [1, 2, 3, 4, 5]
revArray(nums, 0, len(nums)-1)
print(nums)