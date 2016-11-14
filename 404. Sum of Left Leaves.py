# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        result = 0
        stack = []
        node = root

        while node or stack:
            while node:
                if node.left and (not node.left.left) and (not node.left.right):
                    result += node.left.val
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        return result
