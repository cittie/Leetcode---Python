class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        root = num

        while root ** 2 > num:
            root = (root + num / root) >> 1

        return root ** 2 == num
        
