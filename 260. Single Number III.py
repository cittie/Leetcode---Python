class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(operator.xor, nums)
        answer = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [answer, answer ^ xor]