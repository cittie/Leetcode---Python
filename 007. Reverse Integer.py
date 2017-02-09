class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        num = x
        MAX_INT, MIN_INT = (1 << 31) - 1, ~(1 << 31) + 1
        
        if x < 0:
            num = ~num + 1
            
        rev = 0
        
        while num:
            rev *= 10
            rev += num % 10
            num /= 10
        
        if x < 0:
            rev = ~rev + 1
        
        return rev if MIN_INT <= rev <= MAX_INT else 0
