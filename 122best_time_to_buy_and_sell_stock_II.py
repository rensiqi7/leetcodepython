class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        tot = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                tot += prices[i] - prices[i - 1]
        return tot

        """"
        if not prices:
            return 0
        low = high = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                high = prices[i]
            else:
                profit += high - low
                low = high = prices[i]
        profit += high - low
        return profit
        """
