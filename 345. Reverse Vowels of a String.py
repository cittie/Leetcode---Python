class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_list = list(s)
        size = len(s_list)

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vow_sequence = []
        vow_letters = []

        for i in range(size):
            if s_list[i] in vowels:
                vow_sequence.append(i)
                vow_letters.append(s_list[i])

        if vow_sequence:
            vow_sequence.reverse()
            vow_size = len(vow_sequence)
            for j in range(vow_size):
                s_list[vow_sequence[j]] = vow_letters[j]

        return "".join(s_list)
