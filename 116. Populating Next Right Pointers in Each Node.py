# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        stack = []

        if root:
            stack.append([root])

        while stack:
            layer = stack.pop()
            next_layer = []
            n = len(layer)
            for i in range(n):
                node = layer[i]
                if i < n - 1:
                    node.next = layer[i + 1]
                else:
                    node.next = None

                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            if next_layer:
                stack.append(next_layer)
            
