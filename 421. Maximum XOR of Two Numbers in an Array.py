class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Just recite but no very clear about the algorithms.
        mask, result = 0, 0

        for i in range(32)[::-1]:
            mask += 1 << i
            preset = set([num & mask for num in nums])
            current = result | 1 << i
            for pre in preset:
                if current ^ pre in preset:
                    result = current
                    break

        return result
          
