# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return [0, 0]

            left, right = dfs(node.left), dfs(node.right)
            taken = node.val + left[1] + right[1]
            passed = max(left[0], left[1]) + max(right[0], right[1])

            return [taken, passed]

        result = dfs(root)

        return max(result[0], result[1])
        
