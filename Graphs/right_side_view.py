# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node=root):
            right_elements = []
            if not node: return []
            from collections import deque
            q = deque([root])
            while q:
                ans = []
                for _ in range(len(q)):
                    node = q.popleft()
                    ans.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                right_elements.append(ans[-1])
            return right_elements
        return bfs()
            


        