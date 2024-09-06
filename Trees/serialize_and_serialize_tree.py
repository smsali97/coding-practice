# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def rec(node=root):
            if not node:
                res.append('#')
                return
            res.append(str(node.val))
            rec(node.left)
            rec(node.right)
            
        rec()
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.values = data.split(',')
        self.ctr = 0
        def rec():
            value = self.values[self.ctr]
            self.ctr += 1
            if value == '#':
                return None
            else:
                n = TreeNode()
                n.val=value
                n.left = rec()
                n.right = rec()
                return n
        return rec()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))