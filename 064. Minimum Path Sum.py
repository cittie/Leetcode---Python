class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid[0]), len(grid)

        dp = [[0] * m for _ in range(n)]

        for column in range(0, m):
            for row in range(0, n):
                dp[row][column] += grid[row][column]
                if column == 0 and row == 0:
                    continue
                elif column == 0:
                    dp[row][column] += dp[row - 1][column]
                elif row == 0:
                    dp[row][column] += dp[row][column - 1]
                else:
                    dp[row][column] += min(dp[row - 1][column], dp[row][column - 1])

        return dp[-1][-1] if dp else 0
        
