__author__ = 'Cittie'

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        prefix = ''

        for z in zip(*strs):
            if len(set(z)) == 1:
                prefix += z[0]
            else:
                break

        return prefix