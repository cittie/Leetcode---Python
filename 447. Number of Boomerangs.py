class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        result = 0

        for point in points:
            distances = collections.defaultdict(int)

            for target in points:
                distance = (point[0] - target[0]) ** 2 + (point[1] - target[1]) ** 2
                distances[distance] += 1

            for dist in distances:
                result += distances[dist] * (distances[dist] - 1)

        return result
