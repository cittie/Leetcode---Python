class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # http://www.matrix67.com/blog/archives/266
        # For Grey code, the nth num is n xor n right shift 1.

        return [i ^ (i >> 1) for i in range(2 ** n)]
        
