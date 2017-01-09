class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(candidates)
        candidates.sort()
        result = []

        def dfs(nums = [], index = 0):
            total = sum(nums)

            if total == target:
                result.append(nums)
            else:
                for i in range(index, n):
                    cur = candidates[i]
                    if cur + total <= target:
                        dfs(nums + [cur], i)
                    else:
                        break

        dfs()

        return result
        
