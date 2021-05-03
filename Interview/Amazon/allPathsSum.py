'''
Method: Recursion
Time Complexity: O(N^2) N is the number of nodes
Space Complexity: O(NlogN) N is the number of leafs and logN is the maximum depth of a tree
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    # TODO: Write your code here

    find_all_paths(root, sum, [], allPaths)
    return allPaths


def find_all_paths(currnode, targetSum, currpath, allPaths):
    if currnode is None:
        return

    if currnode:
        currpath.append(currnode.val)

    if currnode.val == targetSum and currnode.left is None and currnode.right is None:
        allPaths.append(list(currpath))
    else:
        find_all_paths(currnode.left, targetSum - currnode.val, currpath, allPaths)
        find_all_paths(currnode.right, targetSum - currnode.val, currpath, allPaths)

    del currpath[-1]

    return allPaths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()

