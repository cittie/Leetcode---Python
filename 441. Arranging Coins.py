class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        row, total = 0, 0

        while n >= total:
            row += 1
            total = (row * (row + 1)) >> 1

        return row - 1 if row else row
        
