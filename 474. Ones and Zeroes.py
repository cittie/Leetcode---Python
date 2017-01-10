class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        # dp[zero][one] = max(dp[zero - cur_zero][one - cur_one] + 1, dp[zero][one])
        dp = [[0] * (n + 1) for zero in range(m + 1)]

        for str in strs:
            c_zero, c_one = 0, 0

            for c in str:
                if c == '0':
                    c_zero += 1
                else:
                    c_one += 1

            for zero in range(m, c_zero - 1, -1):
                for one in range(n, c_one - 1, -1):
                    dp[zero][one] = max(dp[zero - c_zero][one - c_one] + 1, dp[zero][one])

        return dp[m][n]
        
