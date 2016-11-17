class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        size_x = len(board)

        for x in range(size_x):
            size_y = len(board[x])
            for y in range(size_y):
                if board[x][y] == 'X':
                    if x > 0 and board[x-1][y] == 'X':
                        continue
                    if y > 0 and board[x][y-1] == 'X':
                        continue
                    count += 1

        return count
