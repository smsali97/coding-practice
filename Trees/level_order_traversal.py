# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root: return []
        q = deque()
        q.append((root,0))
        from collections import defaultdict
        traversed_values = defaultdict(list)
        while q:
            node, level = q.popleft()
            print(level,node.val)
            if node.left:
                q.append( (node.left,level+1) )
            if node.right:
                q.append( (node.right,level+1) )
            traversed_values[level].append(node.val)
        return traversed_values.values()