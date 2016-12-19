class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[-1] >= nums[0]:
            return nums[0]
        else:
            mid = (len(nums) - 1) >> 1      # To reduce time from 155ms to 49ms
            return min(self.findMin(nums[:mid + 1]), self.findMin(nums[mid + 1:]))
