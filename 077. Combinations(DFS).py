class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []

        def dfs(num = 1, nums = []):
            size = len(nums)

            if size == k:
                result.append(nums)
                return
            else:
                for i in range(num + 1, n + 1):
                    dfs(i, nums + [num])


        dfs()

        return result
        
