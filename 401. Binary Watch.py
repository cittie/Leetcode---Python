class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        if num > 8:
            return []

        if num == 0:
            return ["0:00"]

        result = []

        for hour in range(0, 12):
            for minute in range (0, 60):
                count = bin(hour).count('1') + bin(minute).count('1')
                if count == num:
                    result.append(str(hour) + ':' + '{:02d}'.format(minute))

        return result

            
