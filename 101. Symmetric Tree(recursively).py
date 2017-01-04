# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.compare(root.left, root.right) if root else True

    def compare(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            if left.val != right.val:
                return False
            else:
                return self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False
            
