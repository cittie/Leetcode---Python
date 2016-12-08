class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left, right = 0, 0
        counter = collections.defaultdict(int)
        n = len(s)
        result = 0

        while right < n:
            counter[s[right]] += 1
            right += 1
            _max = max(counter.values())

            if right - left > _max + k:
                counter[s[left]] -= 1
                left += 1
            # Moving to left has no chance to get a larger result;
            else:
                result = max(result, right - left)

        return result
        
