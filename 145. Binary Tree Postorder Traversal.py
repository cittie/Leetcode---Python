# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack, result = [], []
        pre = None

        while root or stack:
            if root:
                stack += [root]
                root = root.left
            elif stack[-1].right != pre:
                root = stack[-1].right
                pre = None
            else:
                pre = stack.pop()
                result.append(pre.val)

        return result
        
