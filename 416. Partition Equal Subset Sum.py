class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        target = sum(nums)

        if target & 1:
            return False        # If total is odd
        else:
            target >>= 1        # Even: Transfer to DP, get a subset which sum == total / 2

        dp = collections.defaultdict(bool)
        dp[0] = True

        for num in nums:
            values = dp.keys()
            for val in values:
                current = num + val
                if current == target:
                    return True
                elif current < target:
                    dp[current] = True
                else:
                    dp[(target << 1) - current] = True
        else:
            return False
        
