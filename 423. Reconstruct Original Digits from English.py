class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        uniques = [[0, 'z'], [2, 'w'], [4, 'u'], [6, 'x'], [7, 's'], [8, 'g'], [1, 'o'], [3, 't'], [5, 'f'], [9, 'i']]

        alphabets = collections.defaultdict(int)
        counts = [0] * 10

        for letter in s:
            alphabets[letter] += 1

        for unique in uniques:
            count = alphabets[unique[1]]

            if count > 0:
                counts[unique[0]] = count
                string = nums[unique[0]]
                for char in string:
                    alphabets[char] -= count

        return ''.join([str(i) * counts[i] for i in range(10)])
        
