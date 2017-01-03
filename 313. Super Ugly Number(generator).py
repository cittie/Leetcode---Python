class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        # Learn from the discuss, but I'm not really know how this code works...

        def generate(prime):
            for ugly in uglies:
                yield prime * ugly

        nums = heapq.merge(*map(generate, primes))

        uglies = [1]

        while len(uglies) < n:
            ugly = next(nums)
            if ugly != uglies[-1]:
                uglies.append(ugly)

        return uglies[-1]
        
