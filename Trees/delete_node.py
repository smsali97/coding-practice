# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        def findNode(node=root,parent=None): # return node, and its parent
            if not node: return None, None
            if key == node.val: return node, parent
            parent = node
            if key < node.val: return findNode(node.left,parent)
            else: return findNode(node.right,parent)
        
        node, parent = findNode()
        if not node: return root # no node to delete
        
        # 0 child
        if not node.left and not node.right:
            if not parent:  # Handle the case where the node to be deleted is the root
                return None
            if node.val < parent.val: parent.left = None
            else: parent.right = None
            return root
        
        # 1 child
        if not node.left:
            if not parent:  # Handle the case where the node to be deleted is the root
                return node.right
            if node.val < parent.val: parent.left = node.right
            else: parent.right = node.right
            return root
        if not node.right:
            if not parent:  # Handle the case where the node to be deleted is the root
                return node.left
            if node.val < parent.val: parent.left = node.left
            else: parent.right = node.left
            return root

        # 2 child
        if node.right and node.left:
            successor = node.right
            while successor.left:
                successor = successor.left
            successor_val = successor.val
            node.val = successor.val  # Replace the node's value with the successor's value
            node.right = self.deleteNode(node.right, successor_val)  # Delete the successor node

        return root