class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        size = len(A)
        if size < 3:
            return 0

        result = 0
        arithmetic_length = 0

        delta = A[1] - A[0]

        for i in range(2, size):
            if A[i] - A[i - 1] == delta:
                arithmetic_length += 1
                result += arithmetic_length
            else:
                delta = A[i] - A[i - 1]
                arithmetic_length = 0

        return result
