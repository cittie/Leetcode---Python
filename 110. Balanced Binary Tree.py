# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node, depth):

            if not node:
                return depth

            left, right = dfs(node.left, depth + 1), dfs(node.right, depth + 1)

            return -1 if left == -1 or right == -1 or abs(left - right) > 1 else max(left, right)

        return False if dfs(root, 0) == -1 else True
        
