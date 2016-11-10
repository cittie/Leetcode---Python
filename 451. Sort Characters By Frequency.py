class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}

        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        list = [[k, v] for k, v in dict.items()]
        list.sort(key = operator.itemgetter(1), reverse = True)

        result = ''
        for element in list:
            result += element[0] * element[1]

        return result
