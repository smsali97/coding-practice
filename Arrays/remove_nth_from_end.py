# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        if n == length:
            return head.next
        
        index = length - n - 1 # 5-2=3 -1 = 2 because previous connection will skip it not the curr
        temp = head
        i = 0
        while i < length:
            if i == index:
                temp.next = (temp.next).next if temp.next else None
                i += 2
            else:
                temp = temp.next
                i += 1
        return head

