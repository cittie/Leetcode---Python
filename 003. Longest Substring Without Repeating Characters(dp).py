class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        last_position = collections.defaultdict(int)
        result, start = 0, 0
        
        for i, c in enumerate(s):
            if c not in last_position or last_position[c] < start:
                result = max(result, i - start + 1)
            else:
                start = last_position[c] + 1
            
            last_position[c] = i
            
        return result
