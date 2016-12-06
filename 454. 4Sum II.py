class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        result = 0
        counts = collections.defaultdict(int)

        for a in A:
            for b in B:
                counts[a + b] += 1

        for c in C:
            for d in D:
                result += counts[ - c - d]

        return result
    
