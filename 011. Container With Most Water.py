class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        vol, n = 0, len(height)
        left, right = 0, n - 1

        while left < right:
            vol = max(vol, (right - left) * min(height[right], height[left]))

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return vol
        
