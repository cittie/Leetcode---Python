class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        size = len(nums)
        result = 0

        for num in nums:
            result += abs(num - nums[size / 2])

        return result
        
