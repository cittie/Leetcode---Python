class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for row in range(n >> 1):
            for column in range(row, n - row - 1):
                # swap each two nearby points
                queue = [(column, row), (row, n - 1 - column), (n - 1 - column, n - 1 - row), (n - 1 - row, column)]
                first = queue.pop()
                while queue:
                    second = queue.pop()
                    matrix[first[1]][first[0]], matrix[second[1]][second[0]] = matrix[second[1]][second[0]], matrix[first[1]][first[0]]
