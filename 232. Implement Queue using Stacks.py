class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """

        self._input, self._output = [], []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        self._input.append(x)


    def pop(self):
        """
        :rtype: nothing
        """

        self.peek()
        self._output.pop()


    def peek(self):
        """
        :rtype: int
        """

        if not self._output:
            self._output = self._input[::-1]
            self._input = []

        return self._output[-1]


    def empty(self):
        """
        :rtype: bool
        """

        return not self._output and not self._input

        
