__author__ = 'shye'
class BestTimetoBuyandSellStockIII:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxProfitsForward = []
        maxProfitsBackward = []
        profit = 0
        minPrice = prices[0]
        for curPrice in prices:
            minPrice = min(minPrice, curPrice)
            profit = max(profit, curPrice - minPrice)
            maxProfitsForward.append(profit)

        profit = 0
        maxPrice = prices[-1]
        for curPrice in reversed(prices):
            maxPrice = max(maxPrice, curPrice)
            profit = max(profit, maxPrice-curPrice)
            maxProfitsBackward.insert(0, profit)

        maxProfit = maxProfitsForward[-1]
        for i in range(len(prices) - 1):
            maxProfit = max(maxProfit, maxProfitsForward[i] + maxProfitsBackward[i+1])

        return maxProfit

test = BestTimetoBuyandSellStockIII()
print(test.maxProfit([1,2]))