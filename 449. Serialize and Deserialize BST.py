# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return None

        stack = []
        string = str(root.val)
        stack.append([root])

        while stack:
            current = stack.pop()
            nodes = []
            for node in current:
                if node.left:
                    nodes.append(node.left)
                    string += (',' + str(node.left.val))
                else:
                    string += ',#'
                if node.right:
                    nodes.append(node.right)
                    string += (',' + str(node.right.val))
                else:
                    string += ',#'

            if nodes:
                stack.append(nodes)

        return string


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        data_queue = collections.deque(data.split(','))
        stack = []

        root_val = data_queue.popleft()
        root = TreeNode(int(root_val))
        stack.append([root])

        while stack:
            current = stack.pop()
            nodes = []

            for node in current:
                left = data_queue.popleft()
                if left == '#':
                    node.left = None
                else:
                    node.left = TreeNode(int(left))
                    nodes.append(node.left)

                right = data_queue.popleft()
                if right == '#':
                    node.right = None
                else:
                    node.right = TreeNode(int(right))
                    nodes.append(node.right)

            if nodes:
                stack.append(nodes)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
