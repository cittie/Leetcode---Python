class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        checked, p1, p2, n = 0, 0, 1, len(nums)

        while p1 < n:
            while p2 < n and nums[p1] == nums[p2]:      # Move p2 to the next element
                p2 += 1

            # Put the first element in front
            nums[checked] = nums[p1]
            checked += 1

            if p2 - p1 > 1:     # Check if a duplicate element exists
                nums[checked] = nums[p1]
                checked += 1

            p1, p2 = p2, p2 + 1     # Move the pointers forwards

        return checked if checked < n else n    # Check empty

            
