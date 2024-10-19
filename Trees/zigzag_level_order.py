# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque
        if not root: return []
        q = deque([root])

        level = 0
        elements = []
        while q:
            elements_level = []
            level += 1
            for _ in range(len(q)):
                element = q.popleft()
                elements_level.append(element.val)
                if element.left: q.append(element.left)
                if element.right: q.append(element.right)
            if level % 2 == 0: elements_level = elements_level[::-1]
            elements.append(elements_level)
        return elements

