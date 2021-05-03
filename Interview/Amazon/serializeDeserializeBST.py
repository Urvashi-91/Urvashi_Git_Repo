# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.list = []

        # recursive function declaration
        def dfs(node):
            if not node:
                return
            self.list.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(map(str, self.list))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        list = [int(d) for d in data.split(",")]

        def recurse(list, lower, upper):
            if not list: return None
            if not lower <= list[0] <= upper: return None

            node = list.pop(0)
            root = TreeNode(node)

            root.left = recurse(list, lower, root.val)
            root.right = recurse(list, root.val, upper)

            return root

        return recurse(list, -float("inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans