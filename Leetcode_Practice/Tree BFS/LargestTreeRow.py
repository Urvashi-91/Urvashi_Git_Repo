'''
TC: O(N)
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
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevelMax = float("-inf")
            for _ in range(levelSize):
                currentNode = queue.popleft()
                # add the node to the current level
                currentLevelMax = max(currentLevelMax, currentNode.val)
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(currentLevelMax)

        return result


