class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """

        size = len(str)

        for step in range(1, size):
            if size % step == 0:
                count = size / step
                word = str[:step]
                for i in range(count):
                    if str[i * step: (i + 1) * step] != word:
                        break
                else:
                    return True
        else:
            return False
        
