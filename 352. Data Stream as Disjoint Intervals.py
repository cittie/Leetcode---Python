# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.usedmap = collections.defaultdict(bool)     # True: used; False: unused
        self.imap = collections.defaultdict(bool)         # True: start or end; False: single point


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """

        def checkposition(position):
            if self.imap[position] == True:     # If this point is start or end, delete it
                del(self.imap[position])
            else:                               # Else change it as start or end.
                self.imap[position] = True

        if val not in self.usedmap:
            self.usedmap[val] = True
            if val - 1 in self.usedmap and val + 1 in self.usedmap:
                checkposition(val - 1)
                checkposition(val + 1)
            elif val - 1 in self.usedmap:
                checkposition(val - 1)
                self.imap[val] = True
            elif val + 1 in self.usedmap:
                checkposition(val + 1)
                self.imap[val] = True
            else:
                self.imap[val] = False



    def getIntervals(self):
        """
        :rtype: List[Interval]
        """

        intervals = []

        for key, value in self.imap.items():
            if value == False:
               intervals.append(key)        # If it's a point, record twice.
            intervals.append(key)

        n = len(intervals)
        intervals.sort()

        return [intervals[i:i + 2] for i in range(0, n, 2)]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
