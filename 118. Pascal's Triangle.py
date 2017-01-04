class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows < 1:
            return []

        pTriangle = [[1]]
        n = 2

        while n < numRows + 1:          # n should reach numRows.
            lastRow = pTriangle[-1]
            newRow = []

            for i in range(n - 2):          # width: n - 2
                newRow.append(lastRow[i] + lastRow[i + 1])

            pTriangle.append([1] + newRow + [1])
            n += 1

        return pTriangle
        
