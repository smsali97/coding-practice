# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        from collections import deque
        q = deque([root])
        
        max_so_far = (float('-inf'),-1)
        level = 0
        while q:
            level += 1
            curr_sum = 0   
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
            if curr_sum > max_so_far[0]: max_so_far = (curr_sum, level)
        return max_so_far[1]
