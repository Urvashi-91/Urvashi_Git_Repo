'''
Consensus on the largest integer in the network

Crude algo

Every node has a value variable and maximum variable.
maximum variable gets updated during every traversal.
Every time you arrive at a node, pass parent.maximum.
If: parent.maximum >= current.value, then current.maximum = parent.maximum, and continue traversing the children of current.
Else If: parent.maximum < current.value, then current becomes the new starting point, and repeats whole procedure again.
The loop breaks when all the connected nodes have the same maximum value.
Update
Traversal alg - DFS
If updating every node with the max consensus value is not necessary, then one pass (O(n)) is enough for any graph structure - random connected, tree, etc.
'''
def consensus(root):
    maximum = -float('inf')

    def explore(node):
        if node:
            maximum = max(node.val, maximum)
            for child in node.children:
                explore(child)

    def propogate(node, val):
        if node:
            mode.maximum = val
            for child in node.children:
                propogate(child, val)

    explore(root)
    propogate(maximum)
    return maximum