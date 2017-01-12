class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        max_row = len(matrix)
        if not max_row:
            return 0

        max_column = len(matrix[0])
        if not max_column:
            return 0

        max_lengths = [[0] * max_column for _ in range(max_row)]
        d_r, d_c = [1, -1, 0, 0], [0, 0, 1, -1]

        def search(row, column):
            for i in range(4):
                cur_row, cur_column = row + d_r[i], column + d_c[i]
                if  -1 < cur_row < max_row and -1 < cur_column < max_column and matrix[row][column] < matrix[cur_row][cur_column]:
                    if not max_lengths[cur_row][cur_column]:
                        max_lengths[cur_row][cur_column] = search(cur_row, cur_column)
                    max_lengths[row][column] = max(max_lengths[row][column], max_lengths[cur_row][cur_column] + 1)

            return max_lengths[row][column] if max_lengths[row][column] else 1


        for row in range(max_row):
            for column in range(max_column):
                if not max_lengths[row][column]:
                    max_lengths[row][column] = search(row, column)

        return max([max(row) for row in max_lengths])
