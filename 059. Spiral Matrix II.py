class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0] * n for _ in range(n)]
        current, total, delta = 0, n ** 2, n - 1    # Delta is block width for current circle
        row, column = 0, 0
        col_d = [1, 0, -1, 0]   # Column moving directions
        row_d = [0, 1, 0, -1]   # Row moving directions

        while current < total and delta:
            for d in range(4):
                for _ in range(delta):
                    current += 1
                    matrix[row][column] = current
                    row += row_d[d]
                    column += col_d[d]

            # Moving to next circle
            row += 1
            column += 1
            delta -= 2

        # Check if middle point needs to fill in
        if delta == 0:
            matrix[row][column] = current + 1

        return matrix
