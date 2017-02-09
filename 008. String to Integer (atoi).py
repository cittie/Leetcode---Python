__author__ = 'Cittie'

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        numbers = ''
        symbol = ''
        INT_MAX, INT_MIN = 2147483647, -2147483648

        # Remove extra spaces
        str = str.strip()

        if str[0] in '+-':
            symbol = str[0]
            str = str[1:]

        for c in str:
            if c.isdigit():
                numbers += c
            else:
                break

        num = int(numbers) if numbers else 0

        if symbol == '-':
            num = ~num + 1

        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num
