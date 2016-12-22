class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indexes = {}
        self.nums = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexes:
            return False
        else:
            self.indexes[val] = len(self.nums)
            self.nums.append(val)
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexes:
            last = self.nums[-1]

            self.nums[self.indexes[val]], self.nums[-1] = self.nums[-1], self.nums[self.indexes[val]]
            self.nums.pop()

            self.indexes[last] = self.indexes[val]
            del self.indexes[val]

            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
