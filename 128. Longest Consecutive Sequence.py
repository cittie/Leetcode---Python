class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_map = collections.defaultdict(bool)
        max_length = 0

        for num in nums:
            num_map[num] = True

        for num in num_map:
            if num_map[num]:
                count = 1
                left, right = num - 1, num + 1

                while left in num_map:
                    num_map[left] = False
                    left -= 1
                    count += 1

                while right in num_map:
                    num_map[right] = False
                    right += 1
                    count += 1

                if count > max_length:
                    max_length = count

        return max_length
        
