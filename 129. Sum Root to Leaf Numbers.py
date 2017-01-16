# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        total = {'val' : 0}

        def dfs(node, val):
            if not node.left and not node.right:
                total['val'] += (val * 10 + node.val)
            if node.left:
                dfs(node.left, val * 10 + node.val)
            if node.right:
                dfs(node.right, val * 10 + node.val)

        dfs(root, 0)

        return total['val']
        
