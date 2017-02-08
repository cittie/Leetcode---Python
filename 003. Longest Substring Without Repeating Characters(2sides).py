class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result, start, end = 0, 0, 0
        char_count = collections.defaultdict(int)
        
        for c in s:
            end += 1
            char_count[c] += 1
            
            while char_count[c] > 1:
                char_count[s[start]] -= 1
                start += 1
                
            result = max(result, end - start)
        
        return result
        