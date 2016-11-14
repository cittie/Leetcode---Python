class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_list = list(magazine)

        for char in ransomNote:
            if char in magazine_list:
                magazine_list.remove(char)
            else:
                return False

        return True
