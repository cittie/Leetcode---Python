class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = len(nums)

        for i in range(1, n + 1):
            if nums[-i] == val:
                nums[-i], nums[n - 1] = nums[n - 1], nums[-i]
                n -= 1

        return n
        
