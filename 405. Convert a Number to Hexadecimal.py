class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        result = ''

        if num == 0:
            return '0'
        elif num < 0:
            num += 2 ** 32

        hexs = '0123456789abcdef'

        while num:
            result += hexs[num % 16]
            num /= 16

        return result[::-1]
