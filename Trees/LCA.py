# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # a LCA is when a pivot happens i.e one goes to the left and right
        # also the LCA can also be if p or q is the ancestor itself
        curr = root
        while curr:
            if q.val > curr.val < p.val:
                curr = curr.right
            elif q.val < curr.val > p.val:
                curr = curr.left
            else:
                return curr # if current was the ancestor is also handles 