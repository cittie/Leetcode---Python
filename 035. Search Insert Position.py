class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # return bisect.bisect_left(nums, target)
        # LOL I'm cheating!
        # But you can view https://hg.python.org/cpython/file/2.7/Lib/bisect.py for source.

        n = len(nums)
        left, right = 0, n

        while left < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
        
