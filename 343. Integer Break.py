class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 3:
            return n - 1
            
        mod = n % 3
        result = 0
        
        if mod == 0:
            result = 3 ** (n / 3)
        if mod == 1:
            result = 4 * 3 ** ((n - 1) / 3 - 1)
        if mod == 2:
            result = 2 * 3 ** ((n - 2) / 3)
            
        return result