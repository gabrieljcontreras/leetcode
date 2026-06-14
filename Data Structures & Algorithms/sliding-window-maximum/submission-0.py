from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() #stores the indices of elements
        l = 0
        
        for r in range(len(nums)):
            #pop smaller values from the back of queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r) #add current to the back of queue

            if l > q[0]:  #remove left index from the front if out of bounds
                q.popleft()

            if (r+1) >= k: #record the maximum once you reach size k
                res.append(nums[q[0]])
                l += 1 #slide left boundary forward
        return res