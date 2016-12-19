class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def getMax(nums, left, right):
            if left >= right:
                return nums[left]

            mid = (left + right) / 2
            lmax = getMax(nums, left, mid - 1)
            rmax = getMax(nums, mid + 1, right)

            cmax, mmax = nums[mid], nums[mid]

            for num in nums[left:mid][::-1]:     # [left, mid - 1], descending
                cmax += num
                mmax = max(mmax, cmax)

            cmax = mmax

            for num in nums[mid + 1:right + 1]:         # [mid + 1, right], ascending
                cmax += num
                mmax = max(mmax, cmax)

            return max(lmax, mmax, rmax)

        return getMax(nums, 0, len(nums) - 1)
        
