# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque
        if not root: return 0
        q = deque([(root,0)])

        max_width = 0

        while q:
            level_length = len(q)
            _, level_start = q[0]
            for _ in range(level_length):
                el, idx = q.popleft()
                if el.left: q.append((el.left, 2*idx))
                if el.right: q.append((el.right, 2*idx + 1))
            
            max_width = max(max_width, idx - level_start + 1)
        return max_width
