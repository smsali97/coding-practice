"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        node = head
        prev_node, new_head = None, None
        idx_to_new_node = []
        while node:
            n = Node(node.val)
            idx_to_new_node.append(n)

            if prev_node: prev_node.next = n
            else: new_head = n

            prev_node = n
            node = node.next
        
        node1, node2, = head, new_head
        while node1:
            random_node = node1.random
            if random_node:
                tmp1, tmp2 = head, new_head
                while tmp1 != random_node:
                    tmp1 = tmp1.next
                    tmp2 = tmp2.next
                node2.random = tmp2
            
            node1 = node1.next
            node2 = node2.next
        return new_head

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]

        

        
