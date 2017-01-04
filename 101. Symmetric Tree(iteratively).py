# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = []
        stack.append([root])

        while stack:
            layer = stack.pop()
            next_layer = []
            vals = []

            for node in layer:
                if node:
                    vals.append(node.val)
                    next_layer.append(node.left)
                    next_layer.append(node.right)
                else:
                    vals.append(None)

            if next_layer:
                stack.append(next_layer)
                if vals != vals[::-1]:
                    return False
        else:
            return True
           
