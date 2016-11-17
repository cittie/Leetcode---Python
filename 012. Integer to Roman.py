class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        value_size = len(values)
        numericals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        for i in range(value_size):
            while num >= values[i]:
                num -= values[i]
                result += numericals[i]

        return result
