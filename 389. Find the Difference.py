class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_t = list(t)

        for char in s:
            list_t.remove(char)

        return list_t[0]
