# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    from collections import defaultdict
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        return max(max(ldiameter,rdiameter),lheight+rheight)
        
        
    def height(self,node: TreeNode):
        if not node: return 0
        else: return 1 + max(self.height(node.left),self.height(node.right))