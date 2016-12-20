class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mask, result = 1, 0
        n = len(nums)

        for _ in range(32):
            bitcount = 0

            for num in nums:
                if num & mask:
                    bitcount += 1

            result += bitcount * (n - bitcount)

            mask <<= 1

        return result
        
