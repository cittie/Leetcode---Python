# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

        result = []
        if not root:
            return result

        def dfs(node, s):
            next_s = s + "->" + str(node.val)

            if not node.left and not node.right:
                result.append(next_s)
            if node.left:
                dfs(node.left, next_s)
            if node.right:
                dfs(node.right, next_s)

        if root.left:
            dfs(root.left, str(root.val))
        if root.right:
            dfs(root.right, str(root.val))

        return result if result else [str(root.val)]
        
