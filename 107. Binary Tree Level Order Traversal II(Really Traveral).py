# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        stack, result = [], []

        if root:
            stack.append([root])    # Initial stack

        # If I use result[::-1], the code will be much shorter.

        while stack and stack[-1]:        # Break for the last line
            current = stack[-1]
            nodes = []
            for node in current:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            stack.append(nodes)

        while stack:
            vals = []
            nodes = stack.pop()
            for node in nodes:
                vals.append(node.val)
            if vals:        # The last element in stack is empty, just ignore it.
                result.append(vals)

        return result
             
