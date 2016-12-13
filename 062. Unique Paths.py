class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not n or not m:
            return 0

        dp = [[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            dp[0][i] = 1

        for j in range(n):
            dp[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

        return dp[n - 1][m - 1]
        
