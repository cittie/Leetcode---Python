class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left, right = 0, num

        while left <= right:
            mid = (left + right) >> 1
            if mid ** 2 >= num:
                right = mid - 1
            else:
                left = mid + 1

        return left ** 2 == num
        
