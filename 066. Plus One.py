class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)
        plus = 1

        for i in range(1, n + 1):
            num = digits[-i] + plus
            plus = num / 10
            digits[-i] = num % 10

        return [1] + digits if plus else digits
        
