# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recurse(root, p, q)

    def recurse(self, node, p, q):
        if node is None:
            return

        if node.val == p.val or node.val == q.val:
            return node

        left = self.recurse(node.left, p, q)
        right = self.recurse(node.right, p, q)

        if left is None:
            return right
        if right is None:
            return left

        return node
