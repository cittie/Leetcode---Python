class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        if not t:
            return False

        s_length = len(s)
        t_length = len(t)
        i_s = 0
        i_t = 0

        while i_t < t_length:
            if s[i_s] == t[i_t]:
                if i_s == s_length - 1:
                    return True
                else:
                    i_s += 1
            i_t += 1

        return False

        
