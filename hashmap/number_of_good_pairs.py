#Leetcode-1512 number of Good Pairs
def goodPairs(nums):
    freq = {}
    ans = 0
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    for value in freq.values():
        ans += value*(value - 1)//2
    return ans