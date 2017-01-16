class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        # Throughts from discuss:
        # Each node cos1 1 link and provide 2 link. (except root)
        # So just ensure total links >= 0 in whole progress.

        link = 1
        elements = preorder.split(',')

        for val in elements:
            link -= 1
            if link < 0:
                return False
            if val != '#':
                link += 2

        return True if not preorder or link == 0 else False
        
