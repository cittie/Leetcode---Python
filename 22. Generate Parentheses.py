class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        def dfs(left = 0, right = 0, string = ''):
            if right == n:
                result.append(string)
            if left < n:
                dfs(left + 1, right, string + '(')
            if right < left:
                dfs(left, right + 1, string + ')')

        dfs()

        return result
        
