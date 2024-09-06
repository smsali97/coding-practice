# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next = None
        while curr:
            # temp store next so you dont lose it
            next = curr.next
            
            curr.next = prev

            # move them forward
            prev = curr
            curr = next
        return prev 
