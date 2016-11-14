class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        size = len(s)
        duplicates = []

        for i in range(0, size):
            if s[i] not in duplicates:
                for j in range(i + 1, size):
                    if s[j] == s[i]:
                        duplicates.append(s[i])
                        break;
                else:
                    return i
        else:
            return -1
