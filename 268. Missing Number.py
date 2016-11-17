class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        nums_xor = reduce(operator.xor, nums)
        n_xor = reduce(operator.xor, range(size + 1))

        return 0 ^ nums_xor ^ n_xor
