class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        else:
            return n == 3 ** round(math.log(n, 3))
            
