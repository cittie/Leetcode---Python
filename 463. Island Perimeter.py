class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimetre = 0
        height = len(grid)
        width = len(grid[0])

        for line in range(height):
            for column in range(width):
                if grid[line][column] == 1:
                    perimetre += 4
                    if line < height - 1 and grid[line + 1][column] == 1:
                        perimetre -= 2
                    if column < width - 1 and grid[line][column + 1] == 1:
                        perimetre -= 2

        return perimetre
                    
