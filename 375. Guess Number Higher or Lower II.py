class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for left in range(n - 1, 0, -1):
            for right in range(left + 1, n + 1):
                # Avoid using min() and max() to imporve performance for about 30%
                # Same as dp[left][right] = min(i + max(dp[left][i - 1], dp[i + 1][right]) for i in range(left, right))
                tmp = {'val': 1 << 32}
                for i in range(left, right):
                    val_left, val_right = dp[left][i - 1], dp[i + 1][right]
                    val = i + val_left if val_left > val_right else i + val_right
                    if tmp['val'] > val:
                        tmp['val'] = val
                dp[left][right] = tmp['val']

        return dp[1][n]
        
