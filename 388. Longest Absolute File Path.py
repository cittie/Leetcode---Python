class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        result = 0
        depths = collections.defaultdict(int)

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')
            current_length = depths[depth] + len(name)

            if '.' in name:
                if current_length > result:
                    result = current_length
            else:
                depths[depth + 1] = current_length + 1

        return result
        
