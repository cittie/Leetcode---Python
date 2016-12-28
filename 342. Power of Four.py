class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num > 0 and num & (num - 1) == 0 and num & int('10' * 16, 2) == 0:
            return True
        else:
            return False
        
