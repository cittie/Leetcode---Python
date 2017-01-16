class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [n] * (n + 1)
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 2)]

        for i in range(n + 1):
            if i in squares:
                dp[i] = 1
            else:
                index = 0
                while squares[index] < i:
                    square = squares[index]
                    if dp[i - square] + 1 < dp[i]:
                        dp[i] = dp[i - square] + 1
                    index += 1

        return dp[n]
        
