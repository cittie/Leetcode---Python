class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        width = len(matrix[0])

        for row in matrix:
            left, right = 0, width - 1
            while left <= right:
                mid = (left + right) >> 1
                if row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1
                if row[mid] == target:
                    return True
        else:
            return False
        
