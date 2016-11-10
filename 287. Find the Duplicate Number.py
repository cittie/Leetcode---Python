class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        fast = 0
        slow = 0
        finder = 0

        slow = nums[slow]
        fast = nums[nums[fast]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        while slow != finder:
            slow = nums[slow]
            finder = nums[finder]

        return slow
            