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
        oldtocopy = {None : None}
        curr = head

        while curr:
            oldtocopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr: 
            newNode = oldtocopy[curr]
            newNode.next = oldtocopy[curr.next]
            newNode.random = oldtocopy[curr.random]

            curr = curr.next
        
        return oldtocopy[head]