class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        mask = 0xFFFFFFFF
        max = 0x7FFFFFFF

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a <= max:
            return a
        else:
            return ~(a & max) ^ max
