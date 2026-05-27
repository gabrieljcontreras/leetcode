import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] #min heap of size q

        for num in nums:
            heapq.heappush(self.heap, num)   
            if len(self.heap) > self.k:
                heapq.heappop(self.heap) #evict the smallest

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0] #root always the answer
