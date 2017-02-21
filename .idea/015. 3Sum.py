class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        results = []
        nums.sort()

        for cur in range(n - 2):
            left, right = cur + 1, n - 1

            if cur > 0 and nums[cur] == nums[cur - 1]:
                continue

            while left < right:
                total = nums[cur] + nums[left] + nums[right]

                if total == 0:
                    results.append((nums[cur], nums[left], nums[right]))
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return results