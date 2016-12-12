# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        if not intervals:
            return 0

        intervals.sort(key = operator.attrgetter('end'))
        intervals.sort(key = operator.attrgetter('start'))

        n = len(intervals)
        ends = intervals[0].end
        counts = 1

        for i in intervals:
            if i.start >= ends:
                counts += 1
                ends = i.end
            elif i.end < ends:
                ends = i.end

        return n - counts
        
