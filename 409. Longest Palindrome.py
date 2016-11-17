class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_dict = {}
        pairs_count = 0
        has_mid = False

        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for key, value in char_dict.items():
            if not has_mid and value % 2 == 1:
                has_mid = True
            pairs_count += int(value / 2)

        if has_mid:
            return pairs_count * 2 + 1
        else:
            return pairs_count * 2
