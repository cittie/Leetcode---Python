class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)

        if n < 2:
            return 0
        # buys[i] = max(buys[i - 1], sells[i - 2] - price[i])
        # sells[i] = max(sells[i - 1], buy[i - 1] + price[i])
        buys, sells = [0] * n, [0] * n

        sells[0] = 0
        sells[1] = max(0, prices[1] - prices[0])
        buys[0] = -prices[0]
        buys[1] = max(-prices[0], -prices[1])

        for i in range(2, n):
            buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])
            sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])

        return sells[-1]
        
