class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        result = []

        def dfs(cur_nums = [], index = 0):
            result.append(cur_nums[:])

            for i in range(index, n):
                dfs(cur_nums + [nums[i]], i + 1)

        dfs()

        return result
        
