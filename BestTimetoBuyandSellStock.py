__author__ = 'shye'
class BestTimetoBuyandSellStock:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxProfit = 0
        if len(prices) <= 1:
            return maxProfit
        buyPoint = prices[0]
        sellPoint = buyPoint
        for i in range(1, len(prices)):
            if prices[i] > buyPoint:
                sellPoint = prices[i]
                maxProfit = max(maxProfit, sellPoint-buyPoint)
            else:
                buyPoint = prices[i]
                sellPoint = buyPoint
        return maxProfit

test = BestTimetoBuyandSellStock()
print(test.maxProfit([1,2,3,4,5]))