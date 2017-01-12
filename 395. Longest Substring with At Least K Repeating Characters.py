class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # Got this from discuss in leetcode, it's perfect for python...
        # Maybe I will try another method if possible
        
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(l, k) for l in s.split(c))

        return len(s)
