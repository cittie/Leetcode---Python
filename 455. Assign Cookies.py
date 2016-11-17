class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()

        size_child, size_cookie = len(g), len(s)     # Decrease LTE probability
        child_index, cookie_index, result = 0, 0, 0

        while child_index < size_child and cookie_index < size_cookie:
            if s[cookie_index] >= g[child_index]:
                result += 1
                child_index += 1
            cookie_index += 1

        return result
