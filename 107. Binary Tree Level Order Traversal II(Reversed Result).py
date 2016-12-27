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
            stack.append([root])
            result.append([root.val])

        while stack:
            current = stack.pop()
            nodes, vals = [], []

            for node in current:
                if node.left:
                    nodes.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    nodes.append(node.right)
                    vals.append(node.right.val)

            if nodes:
                stack.append(nodes)
                result.append(vals)

        return result[::-1]
    
