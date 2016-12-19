class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        history_max, current_max = nums[0], 0

        for num in nums:
            if current_max > 0:
                current_max += num
            else:
                current_max = num
            history_max = max(history_max, current_max)

        return history_max
        
