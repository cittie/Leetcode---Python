class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # "incrementing n - 1 elements by 1" == "maximum element decrease 1"

        nums.sort()
        result = 0
        min = nums[0]

        for num in nums:
            result += (num - min)

        return result
