# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head #set the previous pointer initially to null
        while curr: 
            nxt = curr.next #used to store temp variable
            curr.next = prev #reverses to the previous link
            prev = curr #updates previous to be current
            curr = nxt #sets it to saved variable
        return prev #returns the new head
