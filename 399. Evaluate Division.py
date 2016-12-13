class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        result = []
        graph = collections.defaultdict(lambda: collections.defaultdict(float))

        for (l, r), v in zip(equations, values):
            graph[l][r] = v
            graph[r][l] = 1.0 / v

        for m in graph:
            graph[m][m] = 1.0
            for l in graph:
                for r in graph:
                    if graph[l][m] and graph[m][r]:
                        graph[l][r] = graph[l][m] * graph[m][r]

        for l, r in queries:
            if graph[l][r]:
                result.append(graph[l][r])
            else:
                result.append(-1.0)

        return result
