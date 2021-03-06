class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False

        size = len(s) + 1

        flags = [False] * size
        flags[0] = True

        for s_len in range(1, size):
            for i in range(s_len):
                if flags[i] and s[i:s_len] in wordDict:
                    flags[s_len] = True

        return flags[len(s)]
