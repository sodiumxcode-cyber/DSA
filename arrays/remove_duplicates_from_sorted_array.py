#Leetcode-26 Remove duplicates from sorted array
def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k
hehe = removeDuplicates([1, 1, 2])
print(hehe)