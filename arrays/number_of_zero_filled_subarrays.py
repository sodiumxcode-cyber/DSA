#Leetcode-2348
def zeroFilledSubarray(nums):
    count = 0
    result = 0
    for num in nums:
        if num == 0:
            count += 1

        else:
            result += count * (count + 1) // 2
            count = 0
        result += count * (count + 1) // 2
    return result