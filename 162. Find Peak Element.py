class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid_left = (left + right) >> 1
            mid_right = mid_left + 1

            if nums[mid_left] > nums[mid_right]:
                right = mid_left
            else:
                left = mid_right

        return left
        
