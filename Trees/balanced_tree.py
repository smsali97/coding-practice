# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def max_height(node):
            if not node: return 0
            lTree = max_height(node.left)
            rTree = max_height(node.right)

            if abs(lTree - rTree) > 1: self.balanced = False

            return max(lTree,rTree) + 1
        
        max_height(root)
        return self.balanced