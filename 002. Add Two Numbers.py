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
        
        num = l1.val + l2.val
        plus_one = num / 10
        
        node = ListNode(num % 10)
        head = node

        l1, l2 = l1.next, l2.next
        
        while l1 and l2:
            num = l1.val + l2.val + plus_one
            plus_one = num / 10

            node.next = ListNode(num % 10)
            
            l1, l2, node = l1.next, l2.next, node.next

        l = l1 if l1 else l2
        while l:
            num = l.val + plus_one
            plus_one = num / 10
            
            node.next = ListNode(num % 10)
            
            l, node = l.next, node.next
            
        if plus_one:
            node.next = ListNode(plus_one)
            
        return head
