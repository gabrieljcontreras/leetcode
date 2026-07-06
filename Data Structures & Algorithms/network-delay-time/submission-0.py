import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1,n+1)}

        for u,v, w in times:
            adj_list[u].append((v,w))
        min_heap = [(0,k)]
        
        shortest = {}

        while min_heap:
            curr, node = heapq.heappop(min_heap)

            if node in shortest:
                continue

            shortest[node] = curr

            for neighbor, weight in adj_list[node]:
                if neighbor not in shortest:
                    new = curr + weight
                    heapq.heappush(min_heap, (new,neighbor))
        if len(shortest) == n: 
            return max(shortest.values())
        return -1

