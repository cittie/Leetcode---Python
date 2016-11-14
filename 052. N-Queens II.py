class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        positions = [-1] * n
        row = 0
        col = 0
        result = 0
        
        def check_position(row, col):
            for i in range(row):
                if positions[i] == col or abs(row - i) == abs(positions[i] - col):
                    return False
            return True
        
        while row < n:
            while col < n:
                if check_position(row, col):
                    positions[row] = col
                    col = 0
                    break
                else:
                    col += 1
            
            if positions[row] == -1:
                if row == 0:
                    break
                else:
                    row -= 1
                    col = positions[row] + 1
                    positions[row] = -1
                    continue
            
            if row == n - 1:
                result += 1
                col = positions[row] + 1
                positions[row] = -1
                continue
            
            row += 1
            
        return result
