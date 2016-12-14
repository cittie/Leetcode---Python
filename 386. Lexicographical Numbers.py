class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = []
        num = 1

        for _ in range(n):
            result.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                if num >= n:
                    num = num / 10 + 1
                else:
                    num += 1
                while num % 10 == 0:
                    num /= 10

        return result
        
