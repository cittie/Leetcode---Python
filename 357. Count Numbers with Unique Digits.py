class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        results = [1, 10]
        counts = [1, 9]

        for i in range(9):
            counts.append(counts[i + 1] * (9 - i))
            results.append(results[i+ 1] + counts[i + 2])

        if n < 10:
            return results[n]
        else:
            return results[9]
