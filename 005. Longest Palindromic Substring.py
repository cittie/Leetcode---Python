class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ""
            
        n = len(s)
        max_length = 1
        result = s[0]
        
        # for elements
        for i in range(1, n - 1):
            left, right = i - 1, i + 1
            while left > -1 and right < n:
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        result = s[left:right+1]
                        max_length = right - left + 1
                else:
                    break
                
                left -= 1
                right += 1
                    
        # for middle of each 2 elements
        for i in range(n - 1):
            left, right = i, i + 1
            while left > -1 and right < n:
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        result = s[left:right+1]
                        max_length = right - left + 1
                else:
                    break
                
                left -= 1
                right += 1
                
        return result
