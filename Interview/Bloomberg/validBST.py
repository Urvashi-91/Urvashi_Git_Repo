# Definition for a binary tree node.
#TC: O(N) SC: O(N)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, l_bound, r_bound):
            if not node:
                return True
            if not (node.val > l_bound and node.val < r_bound):
                return False

            return (valid(node.left, l_bound, node.val) and valid(node.right, node.val, r_bound))

        return valid(root, float("-inf"), float("inf"))


'''
Method2: Inorder Recursive
'''

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)


'''
Iterative inorder traversal
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True