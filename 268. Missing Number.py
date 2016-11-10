class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_xor = reduce(operator.xor, nums)
        n_xor = reduce(operator.xor, range(len(nums) + 1))
        
        return 0 ^ nums_xor ^ n_xor