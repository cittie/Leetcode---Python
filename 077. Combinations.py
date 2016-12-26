class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # Cheating again now!
        # return [list(element) for element in itertools.combinations(range(1, n + 1), k)]
        # AC! ROFL!!
        # Forget it, let me write the code by myself.

        combinations = []
        pool = range(1, n + 1)
        indices = range(k)

        combinations.append([pool[i] for i in indices])

        while True:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break
            else:
                break

            indices[i] += 1

            for j in range(i + 1, k):
                indices[j] = indices[j - 1] + 1

            combinations.append([pool[i] for i in indices])

        return combinations

# I just recited the algorithm from python source codes.
# But I'm not really know what's happening.
