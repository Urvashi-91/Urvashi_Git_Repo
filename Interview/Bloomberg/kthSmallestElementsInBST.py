'''
Method: Recursive BFS
TC: O(N)
SC: O(N)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

'''
Method2: Iterative
TC: O(H+k)
SC: O(H)
'''
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = deque()
        n = 0
        if root is None:
            return
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            n += 1
            if n == k:
                return node.val
            node = node.right

