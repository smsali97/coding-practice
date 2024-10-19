# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_path(node, target_val, path=[]):
            if not node: 
                return None

            path = path + [node] 
            if node.val == target_val: 
                return path

            path_left = get_path(node.left, target_val, path) 
            if path_left: 
                return path_left 

            path_right = get_path(node.right, target_val, path)
            if path_right:
                return path_right 

            return None

        p_path = get_path(root, p.val)
        q_path = get_path(root, q.val)

        # Optimization: Iterate directly over paths instead of slicing and popping
        for i in range(min(len(p_path), len(q_path)) - 1, -1, -1):
            if p_path[i] == q_path[i]:
                return p_path[i]

        return None
    
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
      return root

    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if l and r:
      return root
    return l or r  # This should ideally never be reached in a valid BST