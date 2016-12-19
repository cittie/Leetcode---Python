class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        count = 0

        val = x ^ y

        while val:
            val &= val - 1
            count += 1

        return count
        
