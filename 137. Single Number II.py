class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        xthrees = 0

        size = len(nums)

        for i in range(size):
            twos |= ones & nums[i]
            ones ^= nums[i]
            xthrees = ~ ( ones & twos)
            twos &= xthrees
            ones &= xthrees

        return ones
