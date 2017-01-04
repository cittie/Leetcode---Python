class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        n = len(nums)

        for i in range(n + 1):      # None and All
            combs = itertools.combinations(nums, i)
            for comb in combs:
                result.append(list(comb))

        return result
        
