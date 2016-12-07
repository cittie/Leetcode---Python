class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # LOL this is cheating though AC.
        # return [list(ele) for ele in itertools.permutations(nums)]

        result = []

        if not nums:
            return None

        size = len(nums)
        indexes = range(size)
        cycles = range(size, 0, -1)

        result.append([nums[i] for i in indexes])

        while True:
            for i in range(size)[::-1]:
                cycles[i] -= 1
                if cycles[i] == 0:
                    indexes[i:] = indexes[i + 1:] + indexes[i: i + 1]
                    cycles[i] = size - i
                else:
                    j = cycles[i]
                    indexes[i], indexes[-j] = indexes[-j], indexes[i]
                    result.append([nums[i] for i in indexes])
                    break
            else:
                return result

        # Codes are copied and revised from python official documents...
        # I don't really understand what's happening...
