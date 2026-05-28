import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones] #set up heap, we negate it since it is maxheap
        heapq.heapify(heap) #rearranges in O(n)

        while len(heap) > 1: #while heap not 1
            y = -heapq.heappop(heap) #pop greatest
            x = -heapq.heappop(heap) #pop second greatest

            if x != y: #only if not equal
                heapq.heappush(heap, -(y-x)) #push back the diff
        
        #return last stone or 0 if nothing remains 
        return -heap[0] if heap else 0 
