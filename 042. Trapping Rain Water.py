class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        n = len(height)

        left, right = 0, n - 1
        volume, min_height = 0, 0

        while left < right:
            while left < right and height[left] <= min_height:
                volume += min_height - height[left]
                left += 1
            while left < right and height[right] <= min_height:
                volume += min_height - height[right]
                right -= 1

            min_height = height[left] if height[left] < height[right] else height[right]

        return volume
    
