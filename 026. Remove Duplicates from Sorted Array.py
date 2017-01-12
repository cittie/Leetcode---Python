class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        correct, n = 1, len(nums)

        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[correct] = nums[i]
                correct += 1

        return correct if correct < n else n    # when n = 0
