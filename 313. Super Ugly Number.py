class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        # Learn from the discuss, but I'm not really know how this code works...

        uglies = [1]
        counts = collections.defaultdict(int)       # Store for corresponding uglies index for each prime
        heap = [(prime, prime) for prime in primes]      # (value, key) for prime list

        while len(uglies) < n:
            (val, prime) = heapq.heappop(heap)      # Get the min element
            counts[prime] += 1

            if val != uglies[-1]:
                uglies.append(val)

            heapq.heappush(heap, (uglies[counts[prime]] * prime, prime))    # Push the next ugly * prime inot heap

        return uglies[-1]
        
