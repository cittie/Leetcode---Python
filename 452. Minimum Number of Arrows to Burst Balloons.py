class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        size = len(points)

        points.sort(key = operator.itemgetter(1))
        points.sort(key = operator.itemgetter(0))
        # Sort firstly by element 0, then element 1;

        cur_pos = points[0][1]
        count = 1

        for i in range(1, size):
            if points[i][0] <= cur_pos:
                cur_pos = min(cur_pos, points[i][1])
            else:
                count += 1
                cur_pos = points[i][1]

        return count
        
