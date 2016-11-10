class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        remaining = 0
        
        for num in nums:
            remaining ^= num
            
        return remaining