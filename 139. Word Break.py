class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False

        flags = [False for i in range(len(s) + 1)]
        flags[0] = True

        for s_len in range(1, len(s) + 1):
            for i in range(s_len):
                if flags[i] and s[i:s_len] in wordDict:
                    flags[s_len] = True

        return flags[len(s)]
