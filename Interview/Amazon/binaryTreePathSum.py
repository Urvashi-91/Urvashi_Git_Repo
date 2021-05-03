'''
Method: recursion
Time Complexity: O(N) N is the number of nodes
Space Complexity: O(D) D is the maximum depth of the tree
'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if root is None:
    return False

  # if the current node is a leaf and its value is equal to the sum, we've found a path
  if root.val == sum and root.left is None and root.right is None:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()


'''
Method: Iteration using Stack
Time Complexity and space Complexity: Same
'''
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        stack = deque()
        stack.append([root, targetSum - root.val])
        # check for leaf node
        while stack:
            node, curr_sum = stack.pop()
            if curr_sum == 0 and node.left is None and node.right is None:
                return True
            if node.right:
                stack.append([node.right, curr_sum - node.right.val])
            if node.left:
                stack.append([node.left, curr_sum - node.left.val])
        return False
