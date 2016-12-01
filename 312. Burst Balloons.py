class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        coins = [1] + nums + [1]
        size = len(coins)
        dp = [[0] * size for i in range(size)]

        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                for middle in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                        dp[left][middle] + coins[left] * coins[middle] * coins[right] + dp[middle][right])

        return dp[0][-1]
        
