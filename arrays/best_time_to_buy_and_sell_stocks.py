#Leetcode 121(Best time to buy and sell stocks)
def StockProfit(prices):
    maxProfit = 0
    bestBuy = prices[0]

    for i in range(0, len(prices)-1):
        if prices[i] > bestBuy:
            maxProfit = max(maxProfit, prices[i]-bestBuy)
        bestBuy = min(bestBuy, prices[i])
    return maxProfit

hehe = StockProfit([7, 1, 3, 8, 4, 5])
print(hehe)