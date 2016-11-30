# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []

        while root:
            stack.append(root)
            root = root.left

        while stack and k > 0:
            node = stack.pop()
            k -= 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left

        return node.val
                
