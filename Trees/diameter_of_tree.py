# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            self.longest_path = 0

            # returns the height
            def recursively_find_height(root) -> int:
                if not root:
                    return 0

                l_tree = recursively_find_height(root.left)
                r_tree = recursively_find_height(root.right)

                current_height = l_tree + r_tree
                self.longest_path = max(current_height,self.longest_path)

                # passing tow the parent
                return max(l_tree,r_tree) + 1

            recursively_find_height(root)
            return self.longest_path


