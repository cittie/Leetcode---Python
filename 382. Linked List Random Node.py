# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = 0
        result = 0

        current = self.head

        while current:
            if random.randint(0, count) == 0:
                result = current.val
            count +=1
            current = current.next

        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
