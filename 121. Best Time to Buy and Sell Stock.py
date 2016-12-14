class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Most common dp.

        if not prices:
            return 0

        n = len(prices)
        buy, sell = -prices[0], 0

        for price in prices:
            sell = max(sell, price + buy)
            buy = max(buy, -price)

        return sell
