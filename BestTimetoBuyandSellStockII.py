__author__ = 'shye'
class BestTimetoBuyandSellStockII:
    # @param prices, a list of integers
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit
