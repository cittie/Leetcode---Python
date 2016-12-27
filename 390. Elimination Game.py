class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, length ,step = 1, n, 1
        right = left + (n - 1) * step

        while length > 1:
            left += step        # Drop the first
            step <<= 1
            length >>= 1
            right = left + (length - 1) * step      # Get the right point.

            left, right = right, left        # Reverse the points with step.
            step = ~step + 1

        return left
        
