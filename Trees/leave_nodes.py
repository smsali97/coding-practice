from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def remove_leaf_nodes(root):
    if not root:
        return []

    # Result to store leaf node layers
    result = []

    # Map to store parent -> children relationships
    parent_to_children = defaultdict(list)
    # Set to store child -> parent relationships
    child_to_parent = {}

    # Initialize the tree structure
    def build_tree_structure(node):
        if not node:
            return
        for child in node.children:
            parent_to_children[node].append(child)
            child_to_parent[child] = node
            build_tree_structure(child)

    build_tree_structure(root)

    # Set to keep track of visited nodes
    visited = set()

    # Function to identify all current leaf nodes
    def find_leaf_nodes():
        leaves = []
        for node, children in parent_to_children.items():
            if node not in visited and len(children) == 0:
                leaves.append(node)
        return leaves

    # BFS-like approach to peel off layers of leaf nodes
    while parent_to_children:
        # Find current leaves
        leaves = find_leaf_nodes()

        if not leaves:
            break

        # Add leaves of this round to result
        result.append([node.value for node in leaves])

        # Mark leaves as visited and remove them from the tree
        for leaf in leaves:
            visited.add(leaf)
            # Remove this leaf from its parent's children list
            if leaf in child_to_parent:
                parent = child_to_parent[leaf]
                parent_to_children[parent].remove(leaf)

        # Remove leaves from parent_to_children
        for leaf in leaves:
            parent_to_children.pop(leaf, None)

    return result

# Example Tree
# Let's say we have a tree like this:
#            1
#         /  |  \
#        2   3   4
#       /|\
#      5 6 7

root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
child1_1 = TreeNode(5)
child1_2 = TreeNode(6)
child1_3 = TreeNode(7)

# Build the tree
root.children = [child1, child2, child3]
child1.children = [child1_1, child1_2, child1_3]

# Execute the function
leaf_layers = remove_leaf_nodes(root)
print(leaf_layers)
