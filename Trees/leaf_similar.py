# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_nodes(node):
            leaf_nodes = []
            if not node: return leaf_nodes
            
            if node.left: leaf_nodes.extend(get_leaf_nodes(node.left))
            if node.right: leaf_nodes.extend(get_leaf_nodes(node.right))
            if not node.right and not node.left: leaf_nodes.append(node.val)

            return leaf_nodes
        l1 = get_leaf_nodes(root1)
        l2 = get_leaf_nodes(root2)
        return l1 == l2
