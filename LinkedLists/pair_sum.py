# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        max_sum = 0
        for i in range(len(arr)//2 + 1):
            max_sum = max(max_sum,arr[i] + arr[-i-1])
        return max_sum
