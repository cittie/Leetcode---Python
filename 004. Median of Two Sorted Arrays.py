class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def bisearch(left, right, m):
            n1, n2 = len(left), len(right)

            if n1 < n2:
                return bisearch(right, left, m)
            if n2 == 0:
                return left[m - 1]
            if m == 1:
                return min(left[0], right[0])

            median2 = min(m >> 1, n2)
            median1 = m - median2

            if left[median1 - 1] < right[median2 - 1]:
                return bisearch(left[median1:], right, m - median1)
            elif left[median1 - 1] > right[median2 - 1]:
                return bisearch(left, right[median2:], m - median2)
            else:
                return left[median1 - 1]

        n = len(nums1) + len(nums2)
        median = (n + 1) >> 1

        if n & 1:
            return bisearch(nums1, nums2, median)
        else:
            return (bisearch(nums1, nums2, median) + bisearch(nums1, nums2, median + 1)) * 0.5
