class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def match(node, seq, index):
    if node is None:
        return False

    if node.val != seq[index] or index >= len(seq):
        return False

    if node.left is None and node.right is None and len(seq) - 1 == index:
        return True

    return match(node.left, seq, index + 1) or match(node.right, seq, index + 1)


def find_path(root, sequence):
    # TODO: Write your code here
    if root is None:
        return len(sequence) == 0
    return match(root, sequence, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
