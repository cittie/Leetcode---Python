class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):

        if sum(nums) < s:
            return 0

        left = 0
        right = len(nums)
        min_count = 0

        while left <= right:
            mid = (left + right) / 2
            if self.solve(mid, s, nums):
                min_count = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_count

    def solve(self, l, s, nums):
        sumZone = 0
        size = len(nums)

        for x in range(size):
            sumZone += nums[x]
            if x >= l:
                sumZone -= nums[x - l]
            if sumZone >= s:
                return True
        return False
