class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []

        def search(num = 0, nums = []):
            count = len(nums)
            total = sum(nums)

            if count > k or total > n:
                return

            if count == k and total == n:
                result.append(nums)
                return

            for i in range(num + 1, 10):
                search(i, nums + [i])

        search()

        return result
