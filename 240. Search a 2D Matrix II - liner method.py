class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        height, width = len(matrix), len(matrix[0])
        row, column = 0, width - 1

        while row < height and column >= 0:
            current = matrix[row][column]
            if current == target:
                return True
            elif current < target:
                row += 1
            else:
                column -= 1
        else:
            return False
