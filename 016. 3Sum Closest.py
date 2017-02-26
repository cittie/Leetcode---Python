class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for cur in range(n - 2):
            left, right = cur + 1, n - 1

            while left < right:
                total = nums[cur] + nums[left] + nums[right]

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

                if abs(total - target) < abs(result - target):
                    result = total

        return result