class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        min, max = 0, len(numbers) - 1

        while min < max:
            if numbers[min] + numbers[max] > target:
                max -= 1
            elif numbers[min] + numbers[max] < target:
                min += 1
            else:
                return [min + 1, max + 1]
