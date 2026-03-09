#Leetcode-122 Best Time to buy and sell stocks II
def maxProfit(prices):
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxProfit = maxProfit + prices[i] - prices[i-1]
    return maxProfit
