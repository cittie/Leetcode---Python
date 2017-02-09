__author__ = 'Cittie'

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        rev_num, num = 0, x

        while num:
            rev_num *= 10
            rev_num += num % 10
            num /= 10

        return rev_num == x
