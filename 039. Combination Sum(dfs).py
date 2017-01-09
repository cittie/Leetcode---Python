class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        result = []
        n = len(candidates)

        def dfs(nums = [], index = 0):
            nums.sort()
            total = sum(nums)

            if total == target:
                result.append(nums)
            else:
                for i in range(index, n):
                    cur = candidates[i]
                    if cur + total <= target:
                        nums.append(cur)
                        dfs(nums[:], i)
                        nums.pop()
                    else:
                        break

        dfs()

        return result
        
