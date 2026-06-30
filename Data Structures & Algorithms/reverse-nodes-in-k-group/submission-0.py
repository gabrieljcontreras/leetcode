# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for i in range(k):
            if not curr: 
                return head
            curr = curr.next
        
        next_group = self.reverseKGroup(curr,k)

        prev = next_group
        curr = head
        count = k

        while count > 0: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count -= 1

        return prev