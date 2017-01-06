class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1

        if not n or nums[-1] > nums[0]:
            return nums[0]
        else:
            return min(self.findMin(nums[:(n >> 1) + 1]), self.findMin(nums[(n >> 1) + 1:]))
        
