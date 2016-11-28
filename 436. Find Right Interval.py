# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        size = len(intervals)
        position_dict = {}
        head_list = []
        result = [-1] * size

        for i in range(size):
            element = intervals[i]
            head_list.append(element.start)
            position_dict[element.start] = i

        head_list.sort()

        for i in range(size):
            element = intervals[i]
            index = bisect.bisect_left(head_list, element.end)
            if index < size:
                key = head_list[index]
                result[i] = position_dict[key]

        return result
