class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1] + [0] * target

        for i in range(target + 1):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]

        return dp[target]
        
