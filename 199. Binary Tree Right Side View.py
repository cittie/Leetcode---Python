# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        queue = collections.deque([root])

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node:
                    if _ == 0:
                        result.append(node.val)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)

        return result
        
