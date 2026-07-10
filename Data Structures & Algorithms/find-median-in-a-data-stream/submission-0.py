import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,val)

        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
    
    def findMedian(self) -> float:
        num = len(self.min_heap)
        num2 = len(self.max_heap)

        total = num + num2

        if total % 2 == 1: 
            return -self.max_heap[0]
        else: 
            min_top = -self.max_heap[0]
            max_top = self.min_heap[0]
            median = (min_top + max_top) / 2
            return median 

        
        