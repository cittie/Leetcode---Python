# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        pre_node, root = head, head.next

        while head and head.next:               # head as left, head.next as right
            next_node = head.next.next          # Move the next node

            if pre_node:                        # Set previous pointer to the right
                pre_node.next = head.next
            head.next.next = head               # Set right pointer to the left
            head.next = next_node               # Set left pointer to the next node

            pre_node = head                     # Move the previous node
            head = next_node                    # Move the head

        return root if root else head
        
