# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, num):
            result = 0

            if not node:
                return result

            if node.val == num:
                result += 1

            result += dfs(node.left, num - node.val)
            result += dfs(node.right, num - node.val)

            return result

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
