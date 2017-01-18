class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex < 2:
            return [1] * (rowIndex + 1)

        row = [1, 1]
        for i in range(rowIndex):
            new_row = []
            for j in range(i):
                new_row.append(row[j] + row[j + 1])
            row = [1] + new_row + [1]

        return row
