class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        max_row = len(matrix)
        if not max_row:
            return

        max_column = len(matrix[0])
        if not max_column:
            return

        zero_row, zero_column = set(), set()

        for row in range(max_row):
            for column in range(max_column):
                if matrix[row][column] == 0:
                    zero_row.add(row)
                    zero_column.add(column)

        for row in zero_row:
            matrix[row] = [0] * max_column


        for row in range(max_row):
            if row in zero_row:
                matrix[row] = [0] * max_column
            else:
                for column in zero_column:
                    matrix[row][column] = 0
