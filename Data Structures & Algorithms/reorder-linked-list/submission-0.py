# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head #declare the fast and slow pointers
        while fast.next and fast.next.next: 
            fast = fast.next.next 
            slow = slow.next
        
        curr = slow.next #we are at the midpoint so we want to reverse this half
        #up to the slow pointer 
        prev = None 
        slow.next = None
        while curr: #reverse linked list 
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt 
        first, second = head, prev  #declare variables to interswap to get new correct list 

        while second: #interswap list 
            temp1 = first.next 
            temp2 = second.next 
            first.next = second
            second.next = temp1
            first = temp1 
            second = temp2