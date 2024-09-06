from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(s, t):
            # Both cannot be different
            if s == None and t == None: return True
            if (s == None) ^ (t == None): return False
            return (
                s.val == t.val
                and is_identical(s.left, t.left)
                and is_identical(s.right, t.right)
            )

        if subRoot is None:
            return True  # An empty subtree is always a subtree of any tree

        if root is None:
            return False  # An empty root cannot contain a non-empty subtree

        if is_identical(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )