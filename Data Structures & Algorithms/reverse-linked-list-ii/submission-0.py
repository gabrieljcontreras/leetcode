# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tailhead = dummy 
        for i in range(left-1): 
            tailhead = tailhead.next

        subhead = tailhead.next

        curr = subhead
        prev = None
        for i in range(right - left +1): 
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt
        subhead.next = curr
        tailhead.next = prev 
        return dummy.next