class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(index + 1)
            else:
                nums[index] = ~nums[index] + 1

        return result
