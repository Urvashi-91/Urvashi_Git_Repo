# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        q = deque()
        q.append(root)
        level_no = 0
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                if level_no % 2 == 0:
                    result.append(level)
                else:
                    level = list(reversed(level))
                    result.append(level)
                level_no += 1
        return result


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result

    q = deque()

    q.append(root)

    count = 2

    while q:
        level = deque()
        qsize = len(q)
        for _ in range(qsize):
            node = q.popleft()
            if node:
                if (count % 2) == 0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        result.append(list(level))
        count += 1

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
