class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        results = []

        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])

                for l in left:
                    for r in right:
                        if c == '+':
                            results.append(l + r)
                        elif c == '-':
                            results.append(l - r)
                        else:
                            results.append(l * r)

        if results:
            return results
        else:
            return [int(input)]
           
