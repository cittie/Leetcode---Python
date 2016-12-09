class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ''
        p = 0

        nums, strings = collections.defaultdict(str), collections.defaultdict(str)

        # When stacks: char[p] = num[p] * char[p + 1]

        for c in s:
            if c.isdigit():
                nums[p] += c
            elif c == '[':
                p += 1
            elif c == ']':
                p -= 1
                strings[p] += int(nums[p]) * strings[p + 1]
                nums[p], strings[p + 1] = '', ''
            else:
                strings[p] += c

        return strings[0]
        
