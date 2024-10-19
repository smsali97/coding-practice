# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

            #     2 +1

            # X       4 +1
            #     10+1    8 +1
            # X   X       4
        self.good_nodes = 0
        if not root: return self.good_nodes

        def rec(node=root,greatest_so_far=root.val):
            if not node: return
            val = node.val
            if val >= greatest_so_far:
                self.good_nodes += 1
            greatest_so_far = max(greatest_so_far,val)
            rec(node.left,greatest_so_far)
            rec(node.right,greatest_so_far)
        rec()
        return self.good_nodes

