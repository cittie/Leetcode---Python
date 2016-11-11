class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        for num in range(n):
            num += 1
            fizzbuzz = ''

            if num % 3 == 0:
                fizzbuzz += 'Fizz'
            if num % 5 == 0:
                fizzbuzz += 'Buzz'

            if len(fizzbuzz) > 0:
                result.append(fizzbuzz)
            else:
                result.append(str(num))

        return result
