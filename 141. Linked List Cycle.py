# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        oneStep, twoStep = head, head

        while oneStep and twoStep and twoStep.next:
            oneStep = oneStep.next
            twoStep = twoStep.next.next
            if oneStep == twoStep:
                return True
        else:
            return False
        
