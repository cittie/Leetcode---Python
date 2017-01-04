class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        max_column = len(board[0])
        max_row = len(board)

        def countNeighbors(row, column):
            count = 0
            # Clockwise moving directions from left top.
            drow = [-1, 0, 0, 1, 1, 0, 0, -1]
            dcol = [-1, 1, 1, 0, 0, -1, -1, 0]

            for i in range(8):
                row += drow[i]
                column += dcol[i]
        #if -1 < row < max_row and -1 < column < max_column:             # This line to enable the edges of the board
                val = board[row % max_row][column % max_column]             # For edgeless version.
                if val == 1 or val == 2:      # Count just for current board.
                    count += 1

            column += 1         # Return to original position.

            '''
            Future stats, & 1 to advance:
            0: 0 -> 0
            1: 1 -> 1
            2: 1 -> 0
            3: 0 -> 1
            '''

            val = board[row][column]
            next_val = bool(1 < count < 4) if val else bool(count == 3)

            if val ^ next_val:      # Status need to change.
                board[row][column] = 3 - val    # 1 to 2; 0 to 3


        for row in range(max_row):
            for column in range(max_column):
                countNeighbors(row, column)

        for row in range(max_row):
            for column in range(max_column):
                board[row][column] &= 1
