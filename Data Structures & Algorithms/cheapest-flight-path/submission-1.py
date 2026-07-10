import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''this solution uses Dijkstra's alg instead of a modified Bellman-Ford's
        except we have to track how many stops we have done to get to a certain dest, 
        not just simply keep track using a visited set, which is what is usually done in a regular Dijsktra's
        algorithm. '''

        adj_list = {i: [] for i in range(n)}
        for u, v, w in flights: 
            adj_list[u].append((v,w))
        
        min_heap = [(0, src, k+1)]

        stops = {}

        while min_heap: 
            cost, node, stops_left = heapq.heappop(min_heap)

            if node == dst: 
                return cost 
            
            if node in stops and stops[node] >= stops_left:
                continue 
            
            stops[node] = stops_left

            if stops_left > 0: 
                for neighbor, price in adj_list[node]:
                    heapq.heappush(min_heap, (cost + price, neighbor, stops_left - 1))
            
        return -1