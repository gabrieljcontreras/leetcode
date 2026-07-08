from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for origin, dest in tickets: 
            adj_list[origin].append(dest)

        for origin in adj_list: 
            adj_list[origin].sort(reverse = True)
        
        itinerary = []

        def dfs(airport):
            while adj_list[airport]:
                next_dest = adj_list[airport].pop()
                dfs(next_dest)
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]