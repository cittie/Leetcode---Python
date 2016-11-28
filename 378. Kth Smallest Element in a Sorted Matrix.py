class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        matrix_expanded = [element for line in matrix for element in line]
        matrix_expanded.sort()

        return matrix_expanded[k - 1]
