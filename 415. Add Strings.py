class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        size1, size2 = len(num1), len(num2)
        size = max(size1, size2) + 1
        num = [0] * size

        for i in range(size):
            digit1, digit2, digit = 0, 0, 0
            if i < size1:
                digit1 = int(num1[- i - 1])
            if i < size2:
                digit2 = int(num2[- i - 1])

            digit = digit1 + digit2 + num[- i - 1]
            if digit > 9:
                num[- i - 2] += 1
                digit -= 10
            num[- i - 1] = digit

        if num[0] == 0:
            num = num[1:]
            
        return ''.join(str(x) for x in num)
