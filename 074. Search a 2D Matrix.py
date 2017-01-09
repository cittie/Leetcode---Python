class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        column = [row[0] for row in matrix]

        left, right = 0, len(column) - 1

        while left <= right:
            mid = (left + right) >> 1
            if column[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        row = matrix[right]

        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) >> 1
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        else:
            return False
            
