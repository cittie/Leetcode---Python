# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return []

        node = head

        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next

        return node
        
