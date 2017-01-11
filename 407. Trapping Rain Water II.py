class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        max_row = len(heightMap)
        if max_row < 3:
            return 0

        max_column = len(heightMap[0])
        if max_column < 3:
            return 0

        volume = 0
        min_heights = []        # (val, row, column)
        d_r, d_c = [0, 0, 1, -1], [1, -1, 0, 0]

        def _heap_push(row, col):
            heapq.heappush(min_heights, (heightMap[row][col], row, col))    # push into heap;
            heightMap[row][col] = ~heightMap[row][col] + 1                  # Use negative to mark as visited;

        # Ignore 4 corners
        heightMap[0][0] = heightMap[0][-1] = heightMap[-1][0] = heightMap[-1][-1] = -1

        # Push all edges to heap
        for row in range(1, max_row - 1):
            _heap_push(row, 0)
            _heap_push(row, max_column - 1)

        for column in range(1, max_column - 1):
            _heap_push(0, column)
            _heap_push(max_row - 1, column)

        while min_heights:
            cur = heapq.heappop(min_heights)
            val, row, column = cur[0], cur[1], cur[2]

            for i in range(4):
                cur_row, cur_col = row + d_r[i], column + d_c[i]

                # Fxck leetcode to use 0 as positive number...
                if -1 < cur_row < max_row and -1 < cur_col < max_column and heightMap[cur_row][cur_col] >= 0:
                    cur_val = heightMap[cur_row][cur_col]
                    if val > cur_val:
                        volume += (val - cur_val)
                        heightMap[cur_row][cur_col] = val
                    _heap_push(cur_row, cur_col)

        return volume
        
