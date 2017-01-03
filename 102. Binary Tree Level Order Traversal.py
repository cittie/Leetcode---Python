# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result, stack = [], []
        stack.append([root])

        while stack:
            layer = stack.pop()
            vals, next_layer = [], []
            for node in layer:
                vals.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            result.append(vals)

            if next_layer:
                stack.append(next_layer)

        return result
                   
