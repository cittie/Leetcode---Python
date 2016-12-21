# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        stack1, stack2= [], []
        last = None
        plusOne = 0

        while l1:
            stack1.append(l1)
            l1 = l1.next

        while l2:
            stack2.append(l2)
            l2 = l2.next

        while stack1 or stack2 or plusOne:

            val1 = stack1.pop().val if stack1 else 0
            val2 = stack2.pop().val if stack2 else 0
            total = val1 + val2 + plusOne

            plusOne = total / 10

            node = ListNode(total % 10)
            node.next = last
            last = node

        return last
        
