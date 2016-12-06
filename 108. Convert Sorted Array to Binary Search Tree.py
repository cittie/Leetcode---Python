# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        current = (len(nums) - 1) / 2
        node = TreeNode(nums[current])

        node.left = self.sortedArrayToBST(nums[:current])
        node.right = self.sortedArrayToBST(nums[current + 1:])

        return node
        
